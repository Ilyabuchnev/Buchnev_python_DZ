
from functools import reduce
def rezult(el, el1):
     return el * el1
print(reduce(rezult, [i for i in range(100, 1001) if i%2 == 0]))



