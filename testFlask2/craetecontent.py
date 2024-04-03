import sqlite3
import hashlib

def create_user(username, password):
    # Подключение к нашей базе данных
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    lst = [
        ['carouselExampleIndicators', 'Slider', 'https://via.placeholder.com/1024x500', 'image 1', 'Title Test 1', 'some text for title 1', 'null', 'null'],
        ['carouselExampleIndicators', 'Slider', 'https://via.placeholder.com/1024x500', 'image 2', 'Title Test 2', 'some text for title 2', 'null', 'null'],
        ['cards', 'miniCards', 'https://via.placeholder.com/150', 'mini imgs 2', 'mini card 2', 'some text for mini card 2', 'null', 'null'],
        ['cards', 'miniCards', 'https://via.placeholder.com/150', 'mini imgs 1', 'mini card 1', 'some text for mini card 1', 'null', 'null']
    ]
    values = []

    for item in lst:
        values.append([item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]])

    c.executemany('INSERT INTO content (idblock, short_title, imgs, altimg, title, contenttext,  author, timestampdata) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', values)
    # Сохранение изменений и закрытие соединения с базой данных
    conn.commit()
    conn.close()

# Замените 'admin' и 'your_password' на желаемые имя пользователя и пароль
create_user('admin', 'your_password')