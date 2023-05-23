import requests
from faker import Faker

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
