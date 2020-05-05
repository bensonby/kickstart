import random

count = 5000000

print('1')
print(count)
print(''.join([str(int(random.random()*10)) for x in range(count)]))
