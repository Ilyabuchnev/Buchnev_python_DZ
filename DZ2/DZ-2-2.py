#Задача 2
a = list(input('Введите числа '))

for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]

print(a)