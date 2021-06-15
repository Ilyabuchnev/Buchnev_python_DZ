# Задача 4
def my_func(x, y):
     return x ** y
  x = int(input("Введите целое число: "))
  y = int(input("Введите его степень, целое отрицательное число: "))
print(my_func(3, -2))

# def my_func(x, y):
#      return 1 if y ==0 else my_func(x, y+1) * 1 /x
# print(my_func(5, -2))