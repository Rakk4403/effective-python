my_foods = ['chocolate', 'cake', 'icecream', 'pizza']

for idx in range(len(my_foods)):
    print('{} : {}'.format(idx, my_foods[idx]))

# it is same output but more readable
for idx, food in my_foods:
    print('{} : {}'.format(idx, food))
