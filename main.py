from flask import Flask, url_for, request, render_template

app = Flask(__name__)


app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 class="anketa">Анкета претендента</h1>
                            <h3 class="anketa">на участие в миссии</h1>

                            <div>
                                <form class="login_form" method="post">
                                <div class="form-group">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                </div>
                                <div class="form-group">    
                                    <label for="classSelect"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                </div>
                                        <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof1" value="Инженер-исследователь">
                                          <label class="form-check-label" for="prof1">
                                            Инженер-исследователь  
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof2" value="Пилот">
                                          <label class="form-check-label" for="prof2">
                                            Пилот 
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof3" value="Строитель">
                                          <label class="form-check-label" for="prof3">
                                            Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof4" value="Экзобиолог">
                                          <label class="form-check-label" for="prof4">
                                            Экзобиолог  
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof5" value="Врач">
                                          <label class="form-check-label" for="prof5">
                                            Врач 
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof6" value="Инженер по терраформированию">
                                          <label class="form-check-label" for="prof6">
                                            Инженер по терраформированию 
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof7" value="Климатолог">
                                          <label class="form-check-label" for="prof7">
                                            Климатолог 
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof8" value="Специалист по радиационной защите">
                                          <label class="form-check-label" for="prof8">
                                            Специалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof9" value="Астрогеолог">
                                          <label class="form-check-label" for="prof9">
                                            Астрогеолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof10" value="Гляциолог">
                                          <label class="form-check-label" for="prof10">
                                            Гляциолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof11" value="Инженер жизнеобеспечения">
                                          <label class="form-check-label" for="prof11">
                                            Инженер жизнеобеспечения
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof12" value="prМетеорологof">
                                          <label class="form-check-label" for="prof12">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof12" value="Оператор марсохода">
                                          <label class="form-check-label" for="prof12">
                                            Оператор марсохода
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof13" value="Киберинженер">
                                          <label class="form-check-label" for="prof13">
                                            Киберинженер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof14" value="Штурман">
                                          <label class="form-check-label" for="prof14">
                                            Штурман
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="prof15" value="Пилот дронов">
                                          <label class="form-check-label" for="prof15">
                                            Пилот дронов
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print('surname-', request.form['surname'])
        print('name-', request.form['name'])
        print('email-', request.form['email'])
        print('class-', request.form['class'])
        print('prof-', request.form['prof'])
        print('sex-', request.form['sex'])
        print('about-', request.form['about'])
        print('file-', request.form['file'])
        print('accept-', request.form['accept'])
        
        return "Форма отправлена"


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
