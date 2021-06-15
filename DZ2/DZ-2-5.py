# Задача 5
a = []
facture = {'название': '','цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [],'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода нажмите Q, для продолжения нажмите Enter ').upper() == 'Q':
        break
    num +=1
    for f in facture.keys():
        prop = input(f'Введите значение свойства {f} ')
        facture[f] = input(prop) if (f == 'цена' or f == 'количество') else prop
        analitics[f].append(facture[f])
    a.append((num, facture.copy()))
    print(f"\nСтруктура товаров\n{a}")
    print(f"\nТекущая аналитика по товарам:\n{'*' * 30}")
    for key, value in analitics.items():
        print(f'{key[:25]:>30}: {value}')
    print('*' * 30)


