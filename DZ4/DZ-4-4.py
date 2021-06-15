
from random import randint

select = [randint(1, 14) for _ in range(14)]
s = select
new_s = []
for i in s:
    if s.count(i) == 1:
        print(i, end=' ')
        new_s.append(i)
#print(select)
