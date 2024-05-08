import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect('database.db')

# Создание курсора
c = conn.cursor()

# Создание таблицы Content
c.execute('''CREATE TABLE IF NOT EXISTS content (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             idblock TEXT,
             short_title TEXT,
             images TEXT,
             altimg TEXT,
             title TEXT,
             contenttext TEXT,
             author TEXT,
             timestampdata DATETIME)''')



c.execute('''CREATE TABLE IF NOT EXISTS User (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             login TEXT,
             fullname TEXT,
             email TEXT,
             number TEXT)
    ''')

# Создание таблицы Users
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT,
             password TEXT,
             role TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS place (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             type TEXT,
             subtype TEXT,
             name TEXT,
             description TEXT,
             subdescription TEXT,
             address TEXT,
             rental_period INTEGER,
             price INTEGER,
             photo_path TEXT,
             locker_rooms TEXT,
             shower TEXT,
             parking TEXT,
             inventory TEXT
             )''')



c.execute('''CREATE TABLE IF NOT EXISTS reservation (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             place_id INTEGER,
             user_id INTEGER,
             start_date TEXT,
             finish_date TEXT,
             FOREIGN KEY(user_id) REFERENCES User(id),
             FOREIGN KEY(place_id) REFERENCES place(id)
             )''')

# c.execute('''DROP TABLE cancellation''')

c.execute('''CREATE TABLE IF NOT EXISTS cancellation (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             reservation_id INTEGER,
             FOREIGN KEY(reservation_id) REFERENCES reservation(id)
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS helper_log (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             branch_id INTEGER,
             user_id INTEGER,
             helper_id INTEGER,
             message TEXT,
             is_question TEXT,
             FOREIGN KEY(user_id) REFERENCES User(id)
             FOREIGN KEY(helper_id) REFERENCES Helper(id)
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Helper (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             login TEXT,
             fullname TEXT,
             FOREIGN KEY(login) REFERENCES users(username)
             )''')

# Закрытие соединения с базой данных
conn.close()