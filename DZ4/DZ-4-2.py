
from random import randint
data = [randint(1, 300) ** 1 for _ in range(13)]
def func_data(lst, n):
    for i in range(1, len(lst), n):
        yield max(lst[i : i + n])
print(list(func_data((data), 2)))
print(data)
