# Задача 1
def division(s1, s2):
    try:
        s1, s2 = int(s1), int(s2)
        division_num = s1/s2
    except ValueError:
        return 'нужно ввести целое положительное число'
    except ZeroDivisionError:
        return 'На 0 делить нельзя'
    return round(division_num, 1)
print(division(input('Введите число '), input('Введите второе число ')))






