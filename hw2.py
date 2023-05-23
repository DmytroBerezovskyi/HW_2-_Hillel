import requests
from faker import Faker
import csv

fake = Faker()
quantity_of_people = 100

for _ in range(quantity_of_people):
    if __name__ == '__main__':
        print(f'{fake.unique.first_name()}: {fake.email()}')

print()

if __name__ == '__main__':
    with open('requirements.txt','r') as file:
        data = file.read()
        print(data)
        print('Parametr for regulation quantity of people: quantity_of_people', quantity_of_people)


r = requests.get('http://api.open-notify.org/astros.json')
if __name__ == '__main__':
    print(f'Number of astronauts: {r.json()["number"]}')


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

avegare_height = height_cm / int(last_index)
avegare_weight = weight_kg / int(last_index)
print(avegare_height)
print(avegare_weight)

