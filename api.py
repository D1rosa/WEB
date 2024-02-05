from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def greet():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promote():
    return """<h1>Человечество вырастает из детства.</h1>
    <h2>Человечеству мала одна планета.</h2>
    <h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
    <h4>И начнем с Марса!</h4>
    <h5>Присоединяйся!</h5>"""


@app.route('/image_mars')
def image():
    return f"""
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/MARS.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
    <h3>Вот она какая, красивая планета.</h3>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
