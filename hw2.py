from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
import requests
from faker import Faker
import csv
from flask import jsonify

app = Flask(__name__)



@app.route("/requirements/")
def requirements():
    with open('requirements.txt','r') as file:
        data = file.read()
    return(data)



@app.route("/generate-users/")
def generate_users():
    return f"""
    <body>Enter the required number of users, the default will be 100 users when you press enter</body>
            <form action="{url_for('fake')}" method ="GET">
                <input type=int, name="input_1">
                <input type="submit">
            </form>
    """
@app.route("/generate-users/fake/", methods=['GET', 'POST'])
def fake(quantity_of_people=100):
    if request.method == 'POST':
        return 'post'
    else:
        fake = Faker()
        if len(request.args.get('input_1')) >= 1:
            try:
                int(request.args.get('input_1'))
            except TypeError:
                print('TypeError')
                return redirect(url_for("generate_users"))
            except ValueError:
                print('ValueError')
                return redirect(url_for("generate_users"))
            else:
                quantity_of_people = int(request.args.get('input_1'))
        else:
            quantity_of_people = 100
        lst = []
        for _ in range(quantity_of_people):
                lst.append(f'{fake.unique.first_name()}: {fake.email()}')
        return lst
@app.route("/")
def urls():
    return f'''
        <html>
    <body>
    
    <h2>ДЗ 2. Flask</h2>
    <p>1. Возвращать содержимое файла с python пакетами (requirements.txt):
    PATH: /requirements/ - открыть файл requirements.txt и вернуть его содержимое:</p>
    <a href="{url_for("requirements")}">Requirements</a><br>
    <p>2. Вывести 100 случайно сгенерированных юзеров (почта + имя)
    Например - 'Dmytro aasdasda@mail.com'
    ( можете использовать - https://pypi.org/project/Faker/ )
    PATH: /generate-users/ + GET параметр который регулирует количество юзеров (/generate-users/?count=100)</p>
    <a href="{url_for("generate_users")}">Generate users</a><br>
    <p>3. Вывести средний рост, средний вес (см, кг) (из приикрепленного файла hw.csv)
    PATH: /mean/
    ОБРАТИТЕ ВНИМАНИЕ НА ЕДЕНИЦЫ ИЗМЕРЕНИЯ</p>
    <a href="{url_for("mean")}">Mean</a><br>
    <p>4. Вывести количество космонавтов в настоящий момент
    (API источник http://api.open-notify.org/astros.json )
    (используйте библиотеку https://pypi.org/project/requests/ )
    PATH: /space/</p>
    <a href="{url_for("space")}">Space</a><br>
    </body>
    </html>
    '''
@app.route("/mean/")
def mean():
    with open('hw.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        height_cm = 0
        weight_kg = 0
        INCH = 2.54
        POUND = 0.45359237
        for row in reader:
            inch_to_cm = float(row[' "Height(Inches)"']) * INCH
            height_cm += inch_to_cm
            pounds_to_kg = float(row[' "Weight(Pounds)"']) * POUND
            weight_kg += pounds_to_kg
            last_index = row['Index']

    average_height = height_cm / int(last_index)
    average_weight = weight_kg / int(last_index)
    # return f'Avegare height:{avegare_height} Avegare weight:{avegare_weight}'
    # return jsonify((f'Avegare height:{avegare_height} cm'
    #                 f'  '
    #                 f'Avegare weight:{avegare_weight} kg'))
    return f'''
                <html>
                <body>
                
                <h2></h2>
                
                <ul>
                  <li>Average&nbspheight:&nbsp;{average_height}&nbsp;cm</li>
                  <li>Average&nbspweight:&nbsp;{average_weight}&nbsp;kg</li>
                </ul>  
                
                </body>
                </html>
             '''


@app.route("/space/")
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return(f'Number of astronauts: {r.json()["number"]}')

if __name__ == '__main__':
    app.run()




