import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["python_db"]
person_collection = db["Persons"]

female = open('knamn.txt', 'r', encoding='utf-8').readlines()
male = open('mnamn.txt', 'r', encoding='utf-8').readlines()
last = open('enamn.txt', 'r', encoding='utf-8').readlines()
street = open('gatunamn.txt', 'r').readlines()
city = open('ortsnamn.txt', 'r').readlines()


def gen_person():
    if random.randint(1, 2) == 1:
        first_name = random.choice(female).strip()
        gender = 'female'
    else:
        first_name = random.choice(male).strip()
        gender = 'male'

    last_name = random.choice(last).strip()
    street_address = random.choice(street).strip().title()
    street_address += " " + str(random.randint(1, 100))
    zip = str(random.randint(100, 999)) + " " + str(random.randint(10, 99))
    city_name = random.choice(city).strip().title()
    return first_name, last_name, gender, street_address, zip, city_name



def main():
    persons = []
    for i in range(1_000_000):
        first_name, last_name, gender, street_address, zip, city_name = gen_person()
        person = {
            'first_name': first_name,
            'last_name': last_name,
            'gender': gender,
            'address': {
                'street_address': street_address,
                'zip': zip,
                'city': city_name
            }
        }
        persons.append(person)
        print("Generated person number", i)

    person_collection.insert_many(persons)

if __name__ == '__main__':
    main()
