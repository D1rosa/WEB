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


@app.route('/promotion_image')
def pr():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-info" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>
    """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
