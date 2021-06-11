# Задача 2

def create_default_user():
    name = str(input('name '))
    surname = str(input('surname '))
    year = int(input('Age'))
    city = str(input('city '))
    email = str(input('email '))
    tel = int(input('tel'))

    return name, surname, year, city, email, tel

name, surname, year, city, email, tel = create_default_user()
print("Name:", name, "surname:", surname, "year:", year, "city:", city, "email:", email, "tel:", tel)