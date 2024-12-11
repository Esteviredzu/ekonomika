import sqlite3

# Инициализация базы данных и создание таблицы
def init_db():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    review TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Получение всех отзывов
def get_reviews():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute("SELECT name, review FROM reviews ORDER BY id DESC")
    reviews = c.fetchall()
    conn.close()
    return reviews

# Добавление нового отзыва
def add_review(name, review):
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute("INSERT INTO reviews (name, review) VALUES (?, ?)", (name, review))
    conn.commit()
    conn.close()
