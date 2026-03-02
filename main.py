from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                  <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/image.gif')}"
           alt="здесь должна была быть картинка, но не нашлась">
           <div>Вот она какая, красная планета.</div>
           </body>
            </html>'''


@app.route('/promotion_image')
def promotion():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                  <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/image.gif')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-secondary" role="alert">
                        Человечество вырастает из детства.</div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.</div>
                    <div class="alert alert-danger" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning" role="alert">
                        И начнем с Марса!</div>
                    <div class="alert alert-dark" role="alert">
                        Присоединяйся!</div>

           </body>
            </html>'''


@app.route('/promotion')
def countdown():
    countdown_list = []
    countdown_list.append('Человечество вырастает из детства.')
    countdown_list.append('Человечеству мала одна планета.')
    countdown_list.append('Мы сделаем обитаемыми безжизненные пока планеты.')
    countdown_list.append('И начнем с Марса!')
    countdown_list.append('Присоединяйся!')
    return '</br>'.join(countdown_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
