#### value types 

x = 5
y = 25

x = y

y = 10

print(x,y)     # -> 25 10


#### reference types

listA = ['Apple','Samsung']
listB = ['Apple','Samsung']

listA = listB

listB[0] = 'Huawei'

print(listA,listB)    # -> ['Huawei', 'Samsung'] ['Huawei', 'Samsung']


