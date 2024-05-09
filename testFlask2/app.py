from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3
import hashlib
import os
import datetime as dt
from datetime import datetime, timedelta
from dbpush import DataPusher
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на ваш секретный ключ

def path_to_save(type, subtype):
    # Путь для сохранения изображений
    path_to_save_images = os.path.join(app.root_path, 'static', 'images', 'catalog', f'{type}', f'{subtype}')
    return path_to_save_images

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def total_price(price, start_date, finish_date):
    if start_date == finish_date:
        return price
    else:
        sd_date = datetime.strptime(start_date, "%d/%m/%Y")
        fd_date = datetime.strptime(finish_date, "%d/%m/%Y")
        difference = fd_date - sd_date
        days_difference = difference.days
        return price * days_difference + price


@app.route('/helper-panel')
def helperpage():
    print(session)
    conn = get_db_connection()
    branch_info = conn.execute(f'''
        SELECT helper_log.branch_id, helper_log.is_question
        FROM helper_log
        WHERE helper_log.helper_id = {session['user_id']}
            AND helper_log.id IN (
                SELECT MAX(id)
                FROM helper_log
                WHERE helper_log.helper_id = {session['user_id']}
                GROUP BY helper_log.branch_id
            );
    ''').fetchall()
    dialog_info = conn.execute(f'''
        SELECT *
        FROM helper_log
        WHERE helper_log.helper_id = {session['user_id']};
    ''').fetchall()
    conn.close()
    json_data={}

    branch_list = [dict(ix) for ix in branch_info]
    dialog_list = [dict(ix) for ix in dialog_info]

    for raw in branch_list:
        # Создание новой записи, если ключ еще не существует
        if 'branch_info' not in json_data:
            json_data['branch_info'] = []

        # Добавление данных в существующий ключ
        json_data['branch_info'].append({
            'branch_id': raw['branch_id'],
            'is_question': raw['is_question']
        })

    for raw in dialog_list:
        # Создание новой записи, если ключ еще не существует
        if 'dialog_info' not in json_data:
            json_data['dialog_info'] = []

        # Добавление данных в существующий ключ
        json_data['dialog_info'].append({
            'id': raw['id'],
            'branch_id': raw['branch_id'],
            'user_id': raw['user_id'],
            'helper_id': raw['helper_id'],
            'message': raw['message'],
            'is_question': raw['is_question']
        })

    print(json_data)
    return render_template('helper_panel.html', json_data=json_data)

@app.route('/profile')
def profilepage():
    print(session)
    conn = get_db_connection()
    user_info = conn.execute(f'''
            SELECT id, fullname, email, number
            FROM User
            WHERE login = "{session['username']}"
        ''').fetchall()
    reservation_info = conn.execute(f'''
        SELECT reservation.id as order_id, place.type, place.subtype, place.name, place.address, place.price, reservation.start_date, reservation.finish_date, place.id as place_id
        FROM place 
        JOIN reservation ON reservation.place_id = place.id
        JOIN User ON User.id = reservation.user_id
        WHERE reservation.user_id = "{session['user_id']}"
    ''').fetchall()
    does_reservation_cancelled = conn.execute(f'''
        SELECT *
        FROM reservation
        WHERE EXISTS (
            SELECT 1
            FROM cancellation
            WHERE cancellation.reservation_id = reservation.id
        )
        AND reservation.user_id = "{session['user_id']}"
    ''').fetchall()
    conn.close()


    cancellation_list = [dict(ix) for ix in does_reservation_cancelled]

    json_data= {}


    # Создание новой записи, если ключ еще не существует
    if 'user_data' not in json_data:
        json_data['user_data'] = []

    # Добавление данных в существующий ключ
    json_data['user_data'].append({
        'id': user_info[0][0],
        'login': session['username'],
        'fullname': user_info[0][1],
        'email': user_info[0][2],
        'number': user_info[0][3],
    })

    blocks_list = [dict(ix) for ix in reservation_info]

    if 'reservation_data' not in json_data:
        json_data['reservation_data'] = []

    for raw in blocks_list:
        # Создание новой записи, если ключ еще не существует
        if 'reservation_data' not in json_data:
            json_data['reservation_data'] = []

        # Добавление данных в существующий ключ
        json_data['reservation_data'].append({
            'order_id': raw['order_id'],
            'type': raw['type'],
            'subtype': raw['subtype'],
            'name': raw['name'],
            'address': raw['address'].split(', '),
            'price': total_price(raw['price'], raw['start_date'], raw['finish_date']),
            'total_days': ((datetime.strptime(raw['finish_date'], "%d/%m/%Y") - datetime.strptime(raw['start_date'], "%d/%m/%Y")).days + 1),
            'start_date': raw['start_date'],
            'finish_date': raw['finish_date'],
            'place_id': raw['place_id'],
            'is_canceled': True if any(raw['order_id'] == item['id'] for item in cancellation_list) else False
        })

    print(json_data)
    return render_template('profile.html', json_data=json_data)


def translate(place_name):

    names = {
        # для кастомных имён сохраняемых картинок
        'Летние площадки': 'summer-sport',
        'Теннисные площадки под открытым небом': 'tennis-outdoor',
        'tennis-outdoor': 'Теннисные площадки под открытым небом',
        'Теннисные площадки под крытым небом': 'tennis-indoor',
        'tennis-indoor': 'Теннисные площадки под крытым небом',
        'Поля для игры в гольф в черте города': 'golf-incity',
        'golf-incity': 'Поля для игры в гольф в черте города',
        'Поля для игры в гольф за чертой города': 'golf-outcity',
        'golf-outcity': 'Поля для игры в гольф за чертой города',
    }

    return names[place_name]


def IsReserved(place_id):
    '''
    Проверяет наличие резервации на площадке за неделю.

    Args:
        place_id (int): Идентификатор площадки, для которой проверяется резервация.

    Returns:
        list: Список списков дат начала и окончания резервации на площадке для указанного place_id, если резервация имеется. В противном случае возвращается False.
    '''
    conn = get_db_connection()
    answer = conn.execute(f'''
        SELECT start_date, finish_date
        FROM reservation
        WHERE place_id = "{place_id}"
    ''').fetchall()
    conn.close()
    if answer:
        dates = []
        for item in answer:
            dates.append([date for date in item])
        return dates
    else:
        return False


def get_dates(isReserved=None):
    '''
    Проверка на резервацию площадки.
    :param isReserved: информация о резервации площадки. Если резервации нет (isReserved=None), возвращаются даты на 7 дней вперед, учитывая сегодня.
    Если резервация имеется на ближайшие дни, возвращаются даты на 7 дней вперед после конца резервации.
    Если резервация имеется на дальние дни, возвращаются даты на дни до начала записанной резервации.
    :return: список дат на основе описанных условий
    '''

    if isReserved:
        dates = []
        sd = isReserved[0][0]
        fd = isReserved[0][1]
        sd_date = datetime.strptime(sd, "%d/%m/%Y")
        fd_date = datetime.strptime(fd, "%d/%m/%Y")
        if (sd_date - datetime.now()).days > 3:
            current_date = datetime.now()
            while current_date < sd_date:
                dates.append(current_date.strftime("%d/%m/%Y"))
                current_date += timedelta(days=1)
            return dates
        else:
            for i in range(8):
                current_date = fd_date + timedelta(days=i+1)
                date_str = current_date.strftime("%d/%m/%Y")
                dates.append(date_str)

            return dates
    else:
        dates = []
        today = datetime.now()

        for i in range(8):
            current_date = today + timedelta(days=i)
            date_str = current_date.strftime("%d/%m/%Y")
            dates.append(date_str)

        return dates


@app.route('/cancelation_form', methods=['POST'])
def cancelation_form():
    if request.method == 'POST':
        reservation_id = request.form['reservation_id']
        with DataPusher('database.db') as changer:
            changer.insert_data(table='cancellation', reservation_id=reservation_id)
        # Тут надо всплывающее окно типа "Погодите, админ получил заявку на отмену!"
        return redirect(url_for('profilepage'))

from flask import jsonify

@app.route('/submit_message', methods=['POST'])
def submit_message():
    message = request.json['message']
    senderId = request.json['senderId']

    # Надо продумать логику когда обновлять ветку и как выбирать хелперов
    conn = get_db_connection()
    user_id = session['user_id'] if 'user_id' in session else 0
    # если есть ветка для такго юзера, берём её, если нет, то создаём новую
    branch_id = conn.execute(f'''SELECT branch_id FROM helper_log WHERE user_id = {user_id}''').fetchone()[0] if conn.execute(f'''SELECT branch_id FROM helper_log WHERE user_id = {user_id}''').fetchone() else ((conn.execute(f'''SELECT MAX(branch_id) AS max_branch_id FROM helper_log''').fetchone()[0])+1)
    helper_id = 1
    conn.close()

    with DataPusher('database.db') as changer:
        changer.insert_data(table='helper_log', branch_id=branch_id , user_id=user_id, helper_id=helper_id, message=message, is_question='True')


    return jsonify({'status': 'success'})


@app.route('/get_messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    u_id = session['user_id'] if 'user_id' in session else 0
    messages = conn.execute(f'''
        SELECT message, is_question
        FROM helper_log
        WHERE user_id = {u_id} AND helper_id=1
    ''').fetchall()

    conn.close()

    html = ''
    for message in messages:
        if message[1] == 'True':
            html += f"<li class='chat outgoing'><p>{message[0]}</p></li>"
        else:
            html += f"<li class='chat incoming'><span class='material-symbols-outlined'>smart_toy</span><p>{message[0]}</p></li>"
    return html






@app.route('/submit_message_helper', methods=['POST'])
def submit_message_helper():
    message = request.json['message']
    branchId = request.json['branchId']
    # Надо продумать логику когда обновлять ветку и как выбирать юзера

    conn = get_db_connection()
    info = conn.execute(f'''
                SELECT user_id, helper_id
                FROM helper_log
                WHERE branch_id = {branchId}
            ''').fetchone()
    conn.close()


    branch_id = branchId
    user_id = info[0]
    helper_id = info[1]
    print(branchId, user_id, helper_id)
    with DataPusher('database.db') as changer:
        changer.insert_data(table='helper_log', branch_id=branch_id , user_id=user_id, helper_id=helper_id, message=message, is_question='False')


    return jsonify({'status': 'success'})


@app.route('/get_messages_helper', methods=['GET'])
def get_messages_helper():
    branch_id = request.args.get('branch_id')
    current_branch = branch_id if branch_id is not None else None

    conn = get_db_connection()
    messages = conn.execute(f'''
        SELECT message, is_question
        FROM helper_log
        WHERE branch_id = {current_branch}
    ''').fetchall()
    conn.close()

    html = ''
    for message in messages:
        if message[1] == 'True':
            html += f"<li class='chat incoming'><span class=\"material-symbols-outlined\"><img class=\"ic_finished_orders\" src=\"../static/images/svg-files/user.svg\" style=\"width: 30px; height: 30px;\" alt=\"\"></span><p>{message[0]}</p></li>"
        else:
            html += f"<li class='chat outgoing'><p>{message[0]}</p></li>"
    html += f"<input type=\"hidden\" id=\"branch-id\" name=\"branchId\" value=\"{current_branch}\"> "
    return html


@app.route('/handle_form', methods=['POST'])
def handle_form():
    print(session)
    if 'user_id' in session:
        if request.method == 'POST':
            for key in request.form:
                if key.startswith('start_date_') and key.endswith('_l'):
                    place_id = key.split('_')[2]  # получаем id из имени поля
                    start_date = request.form[key]
                    finish_date = request.form[f'finish_date_{place_id}_l']
                    if start_date!='0' and finish_date!='0':
                        with DataPusher('database.db') as changer:
                            changer.insert_data(table='reservation', place_id=int(place_id), user_id=session['user_id'],
                                                start_date=start_date, finish_date=finish_date)
                if key.startswith('start_date_') and key.endswith('_r'):
                    place_id = key.split('_')[2]  # получаем id из имени поля
                    start_date = request.form[key]
                    finish_date = request.form[f'finish_date_{place_id}_r']
                    if start_date!='0' and finish_date!='0':
                        with DataPusher('database.db') as changer:
                            changer.insert_data(table='reservation', place_id=int(place_id), user_id=session['user_id'],
                                                start_date=start_date, finish_date=finish_date)
            return redirect(url_for('profilepage'))
    else:
        return redirect(url_for('login'))

@app.route('/catalog-page/<place_name>')
def catalog(place_name):
    print(session)
    print(IsReserved(1))
    subtype = translate(place_name)
    conn = get_db_connection()

    subtype_places_info = conn.execute(f'''
        SELECT * 
        FROM place    
        WHERE subtype = "{subtype}"
    ''').fetchall()

    conn.close()

    blocks_list = [dict(ix) for ix in subtype_places_info]
    # print(blocks_list) [{строка 1 из бд},{строка 2 из бд},{строка 3 из бд}, строка 4 из бд]

    for block in blocks_list:

        if '\n' in block['subdescription']:

            block['subdescription'] = block['subdescription'].split('\n')
        else:
            block['subdescription'] = [block['subdescription']]

    # Теперь нужно сделать группировку списка в один словарь json
    # Группировка данных в словарь JSON
    json_data = {}
    for raw in blocks_list:
        # Создание новой записи, если ключ еще не существует
        if raw['subtype'] not in json_data:
            json_data[raw['subtype']] = []

        # Добавление данных в существующий ключ
        json_data[raw['subtype']].append({
            'id': raw['id'],
            'name': raw['name'],
            'description': raw['description'],
            'subdescription': raw['subdescription'],
            'address': raw['address'],
            'rental_period': raw['rental_period'],
            'price': raw['price'],
            'photo_path': raw['photo_path'],
            'locker_rooms': raw['locker_rooms'],
            'shower': raw['shower'],
            'parking': raw['parking'],
            'inventory': raw['inventory'],
            'start_date': get_dates(IsReserved(raw['id'])),
            'finish_date': get_dates(IsReserved(raw['id']))
        })
    print(json_data)
    return render_template(f'selected-places.html', place_name=subtype, json_data=json_data)

@app.route('/catalog-page')
def catalogpage():
    print(session)
    conn = get_db_connection()
    place_info = conn.execute('''
            SELECT type, GROUP_CONCAT(DISTINCT subtype) AS subtypes
            FROM place
            GROUP BY type
        ''').fetchall()
    conn.close()

    path_photo_list = []


    for it in place_info:
        print([i for i in it])
    json_data = {'place_list': []}
    for row in place_info:
        json_data['place_list'].append({
            'type': [row['type'], translate(row['type'])],
            'subtypes': [(item[0], item[1]) for item in zip(row['subtypes'].split(','), [translate(subtypes) for subtypes in row['subtypes'].split(',')]) if row['subtypes']]
        })

    print(json_data)
    return render_template('catalog.html', json_data=json_data, sender_id=session['user_id'] if 'user_id' in session else 0)


@app.route('/registration', methods=['GET', 'POST'])
def signup():
    print(session)
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        second_password = request.form['second_password']
        email = request.form['email']
        fullname = request.form['fullname']
        phone_number = request.form['number']
        if password != second_password:
            error = 'Пароли не совпадают!'
            print(error)
            return render_template('registration.html', error=error)

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user:
            error = 'Пользователь с таким логином уже зарегестрирован!'
            print(error)
            return render_template('registration.html', error=error)
        if not user:
            conn = get_db_connection()
            c = conn.cursor()

            # Вставка данных в таблицу "users"
            hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            values_users = (username, hash_password, 'user')
            c.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', values_users)
            conn.commit()

            # Вставка данных в таблицу "User"
            values_User = (username, fullname, email, phone_number)

            c.execute(
                'INSERT INTO User (login, fullname, email, number) VALUES (?, ?, ?, ?)',
                values_User)
            conn.commit()

            conn.close()

            session['username'] = username
            # session['user_id'] = user['id']
            session['role'] = 'user'
            session['logged_in'] = True
            session.modified = True  # Пометить сессию как измененную

            print('Yeap, USER')
            print(session)
            # redirect to user page (может быть на пршлую страницу, где был юзер)
            return redirect(url_for('profilepage'))


        else:
            error = 'Неправильное имя пользователя или пароль'

    return render_template('registration.html', error=error)


@app.route('/')
def main_page():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    print(session)
    if 'username' in session:
        if session['role'] == 'user':
            return redirect(url_for('profilepage'))
        elif session['role'] == 'helper':
            return redirect(url_for('baristapage'))
        elif session['role'] == 'admin':
            return redirect(url_for('adminpage'))

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        # uuser = User(user['username'])
        if user:
            session['username'] = user['username']
            print(session)
            if user and user['password'] == hashed_password and user['role'] == 'user':
                conn = get_db_connection()
                user_id = conn.execute('SELECT id FROM User WHERE login = ?', (username,)).fetchone()
                conn.close()
                session['user_id'] = user_id['id']
                session['role'] = user['role']
                session['logged_in'] = True
                session.modified = True  # Пометить сессию как измененную
                print('Yeap, USER')
                # redirect to user page (может быть на пршлую страницу, где был юзер)
                return redirect(url_for('profilepage'))

            elif user and user['password'] == hashed_password and user['role'] == 'admin':
                session['user_id'] = user['id']
                session['role'] = user['role']
                print('Yeap, ADMIN')
                # redirect to admin page - информация о всём + ребилд инфы на страницах (например новое летнее меню)
                return redirect(url_for('adminpage'))

            elif user and user['password'] == hashed_password and user['role'] == 'helper':
                conn = get_db_connection()
                user_id = conn.execute('SELECT id FROM Helper WHERE login = ?', (username,)).fetchone()
                conn.close()
                session['user_id'] = user_id['id']
                session['role'] = user['role']

                print('Yeap, HELPER')
                # redirect to barista page - информация о заказах (которые сегодня)
                return redirect(url_for('helperpage'))

            else:
                error = 'Неправильное имя пользователя или пароль'
        else:
            error = 'Такого нет аккаунта'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # Удаление данных пользователя из сессии
    session.clear()
    # Перенаправление на главную страницу или страницу входа
    return redirect(url_for('main_page'))



@app.route('/update_content', methods=['POST'])
def update_content():

    imgpath = None
    content_id = request.form['id']
    short_title = request.form['short_title']
    title = request.form['title']
    altimg = request.form['altimg']
    contenttext = request.form['contenttext']

    # Обработка загруженного файла
    file = request.files['img']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(path_to_save_images, filename)
        imgpath = "/static/images/"+filename
        file.save(save_path)
        # Обновите путь изображения в вашей базе данных

    # Обновление данных в базе
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    print(short_title, imgpath, altimg, title, contenttext, content_id)
    cursor.execute('UPDATE content SET short_title=?, img=?, altimg=?, title=?, contenttext=? WHERE id=?',
                   (short_title, imgpath, altimg, title, contenttext, content_id))
    # if file:
    #     cursor.execute('UPDATE content SET short_title=?, img=?, altimg=?, title=?, contenttext=? WHERE id=?',
    #                (short_title, imgpath, altimg, title, contenttext, content_id))
    # else:
    #     cursor.execute('UPDATE content SET short_title=?, altimg=?, title=?, contenttext=? WHERE id=?',
    #                    (short_title, altimg, title, contenttext, content_id))
    conn.commit()
    conn.close()

    return redirect(url_for('admin_panel'))

@app.route('/cancellation_requests', methods=['POST'])
def cancellation_requests():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'cancel_reservation':
            reservation_id = request.form['reservation_id']
            cancellation_id = request.form['cancellation_id']
            with DataPusher('database.db') as changer:
                changer.delete_data(table='reservation', ID=int(reservation_id))
                changer.delete_data(table='cancellation', ID=int(cancellation_id))
        elif action == 'cancel_cancellation':
            cancellation_id = request.form['cancellation_id']
            with DataPusher('database.db') as changer:
                changer.delete_data(table='cancellation', ID=int(cancellation_id))
    return redirect(url_for('adminpage'))

@app.route('/place_action', methods=['POST'])
def placeaction():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'add':
            type = request.form['type']
            subtype = request.form['subtype']
            name = request.form['name']
            address = request.form['address']
            description = request.form['description']
            subdescription = request.form['subdescription']
            rental_period = request.form['rental_period']
            price = request.form['price']

            if 'photo_path' not in request.files:
                return 'No file part'

            image_file = request.files['photo_path']

            if image_file.filename == '':
                return 'No selected file'
            file_path='None'
            if image_file:
                conn = get_db_connection()
                photo_id = conn.execute(f'''SELECT COUNT(*) id FROM place WHERE type = "{type}" AND subtype = "{subtype}"''').fetchall()
                conn.close()
                # Генерируем новое имя файла
                filename = f'{translate(subtype)}-item-{photo_id[0][0]+1}.jpg'  # Здесь можно использовать любое желаемое имя
                # Формируем путь для сохранения
                file_path = os.path.join(path_to_save(translate(type),translate(subtype)), filename)
                # Сохраняем файл
                image_file.save(file_path)
            flag = False
            path = file_path.split('\\')
            new_file_path = '../'
            for item in path:
                if item == 'static':
                    flag = True
                if flag:
                    new_file_path += item + '/'
            if new_file_path.endswith('/'):
                new_file_path = new_file_path[:-1]
            if 'locker_room' in request.form:
                locker_room = 'True'
            else:
                locker_room = 'False'
            if 'shower' in request.form:
                shower = 'True'
            else:
                shower = 'False'
            if 'parking' in request.form:
                parking = 'True'
            else:
                parking = 'False'
            if 'inventory' in request.form:
                inventory = 'True'
            else:
                inventory = 'False'
            # надо ещё проверить все на ввод!!!
            with DataPusher('database.db') as changer:
                changer.insert_data(table='place', type=f'{type}', subtype=f'{subtype}', name=f'{name}', description=f'{description}',
                                    subdescription=f'{subdescription}', address=f'{address}', rental_period=int(rental_period), price=int(price),
                                    photo_path=f'{new_file_path}', locker_rooms=f'{locker_room}', shower=f'{shower}', parking=f'{parking}', inventory=f'{inventory}')
        elif action == 'change':
            type = request.form['type']
            subtype = request.form['subtype']
            name = request.form['name']
            conn = get_db_connection()
            place_info = conn.execute(f'''SELECT * FROM place WHERE type = "{type}" AND subtype="{subtype}" AND name="{name}"''').fetchone()
            conn.close()
            new_description = request.form.get('description')
            if new_description is None or new_description.strip() == '':
                new_description = place_info['description']
            new_subdescription = request.form.get('subdescription')
            if new_subdescription is None or new_subdescription.strip() == '':
                new_subdescription = place_info['subdescription']
            new_address = request.form.get('address')
            if new_address is None or new_address.strip() == '':
                new_address = place_info['address']
            new_rental_period = request.form.get('rental_period')
            if new_rental_period is None or new_rental_period.strip() == '':
                new_rental_period = place_info['rental_period']
            new_price = request.form.get('price')
            if new_price is None or new_price.strip() == '':
                new_price = place_info['price']
            if 'photo_path' in request.files:
                image_file = request.files['photo_path']
                # Проверяем, что файл не пустой
                if image_file and image_file.filename != '':
                    photo_name = place_info['photo_path']
                    file_path = os.path.join(path_to_save(translate(type), translate(subtype)), photo_name.split('/')[-1])
                    print(file_path)
                    image_file.save(file_path)
                    new_photo_path = place_info['photo_path']
                else:
                    new_photo_path = place_info['photo_path']
            else:
                new_photo_path = place_info['photo_path']

            if 'locker_room' in request.form:
                new_locker_room = 'True'
            else:
                new_locker_room = 'False'

            if 'shower' in request.form:
                new_shower = 'True'
            else:
                new_shower = 'False'
            if 'parking' in request.form:
                new_parking = 'True'
            else:
                new_parking = 'False'
            if 'inventory' in request.form:
                new_inventory = 'True'
            else:
                new_inventory = 'False'

            with DataPusher('database.db') as changer:
                changer.update_data(table='place', ID=f'{place_info['id']}', type=f'{type}', subtype=f'{subtype}', name=f'{name}', description=f'{new_description}',
                                    subdescription=f'{new_subdescription}', address=f'{new_address}', rental_period=int(new_rental_period), price=int(new_price),
                                    photo_path=f'{new_photo_path}', locker_rooms=f'{new_locker_room}', shower=f'{new_shower}', parking=f'{new_parking}', inventory=f'{new_inventory}')
        elif action == 'delete':
            type = request.form['type']
            subtype = request.form['subtype']
            name = request.form['name']
            conn = get_db_connection()
            place_info = conn.execute(
                f'''SELECT * FROM place WHERE type = "{type}" AND subtype="{subtype}" AND name="{name}"''').fetchone()
            conn.close()
            with DataPusher('database.db') as changer:
                changer.delete_data(table='place', ID=f'{place_info['id']}')

    return redirect(url_for('adminpage'))


@app.route('/admin_panel' )
def adminpage():
    conn = get_db_connection()
    place_info = conn.execute('''
        SELECT type, subtype, STRING_AGG(name, ',') AS names
        FROM place
        GROUP BY type, subtype
    ''').fetchall()
    cancel_info = conn.execute('''
        SELECT cancellation.id as cancellation_id, cancellation.reservation_id as reservation_id, reservation.place_id as place_id, reservation.user_id as user_id, reservation.start_date as start_date, reservation.finish_date as finish_date, place.type as type, place.subtype as subtype, place.name as name, User.fullname as fullname, User.number as number, User.email as email
        FROM cancellation
        JOIN reservation ON reservation.id = cancellation.reservation_id
        JOIN place ON place.id = reservation.place_id
        JOIN User ON User.id = reservation.user_id
        WHERE reservation.id = cancellation.reservation_id
    ''').fetchall()
    # timeout_resrvation = cancel_info = conn.execute('''
    #     SELECT reservation.id, reservation.place_id as place_id, reservation.user_id as user_id, reservation.start_date as start_date, reservation.finish_date as finish_date, place.type as type, place.subtype as subtype, place.name as name, User.fullname as fullname, User.number as number, User.email as email
    #     FROM reservation
    #     JOIN place ON place.id = reservation.place_id
    #     JOIN User ON User.id = reservation.user_id
    #     WHERE reservation.finish_date = cancellation.reservation_id
    # ''').fetchall()
    conn.close()

    cancel_list = [dict(ix) for ix in cancel_info]
    json_data = {'place_list': []}

    for row in place_info:
        json_data['place_list'].append({
            'type': row['type'],
            'subtype': [{
                'name': row['subtype'],
                'names': row['names'].split(',') if row['names'] else []
            }]
        })

    for raw in cancel_list:
        # Создание новой записи, если ключ еще не существует
        if 'cancel_list' not in json_data:
            json_data['cancel_list'] = []

        # Добавление данных в существующий ключ
        json_data['cancel_list'].append({
            'cancellation_id': raw['cancellation_id'],
            'reservation_id': raw['reservation_id'],
            'place_id': raw['place_id'],
            'user_id': raw['user_id'],
            'start_date': raw['start_date'],
            'finish_date': raw['finish_date'],
            'type': raw['type'],
            'subtype': raw['subtype'],
            'name': raw['name'],
            'fullname': raw['fullname'],
            'number': raw['number'],
            'email': raw['email'],
            'reason': 'cancel'
        })


    print(json_data)

    return render_template('admin_panel.html', json_data=json_data)

if __name__ == '__main__':
    app.run(debug=True)
