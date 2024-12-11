import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from database import get_reviews, add_review, init_db
from products import products


app = Flask(__name__)
app.secret_key = 'your_secret_key'

init_db()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/assortment')
def assortment():
    return render_template('assortment.html', products=products)

@app.route('/reviews', methods=['GET'])
def reviews():
    reviews = get_reviews()  # Получаем все отзывы из базы данных
    return render_template('reviews.html', reviews=reviews)


@app.route('/add_review', methods=['POST'])  # Новый маршрут для добавления отзыва
def add_review_route():
    name = request.form.get('name')
    review = request.form.get('review')

    if not name or not review:
        return jsonify({"message": "Пожалуйста, заполните все поля!"}), 400

    # Сохранение отзыва в базе данных
    add_review(name, review)

    # Перенаправляем пользователя на страницу с отзывами после добавления
    flash('Отзыв добавлен успешно!')  # Используем Flask flash для вывода сообщения
    return redirect(url_for('index'))  # Перенаправляем на главную страницу

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4141, debug=True, ssl_context=('certificate.crt', 'private.key'))
