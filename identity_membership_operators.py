# Identity Operator : is
# Comparing references

x = y = [1,2,3]
z = [1,2,3]
t = [2,4]

print(x==y)     # True
print(x==z)     # True

print(x is y)   # True
print(x is z)   # False
print(x is not z)   # True

# Membership Operator : in

k = ['apple','banana']
print('banana' in k)  # True
print('banana' not in k)  # False


