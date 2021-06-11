# Задача 6
def my_funk(earth):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return earth.title() if not set(earth).difference(latin_char) else False
earth = input('Введите слова разделенные пробелами ').split()
for e in earth:
    result = my_funk(e)
    if result:
        print(my_funk(e))


