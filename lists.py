#### lists

my_list = [1,2,3]
my_list2 = ['one',2,True,6.5]

list1 = ['one','two','three']
list2 = ['four','five','six']

print((list1+list2)[3])       # returns 'four'

userA = ['Emre',24]
userB = ['İrfan',38]

users = userA + userB        

print(users)                  # returns ['Emre', 24, 'İrfan', 38]

users2D = [userA,userB]

print(users2D[1][1])          # returns 38


#### lists examples

# 1- create a list with "Bmw, Mercedes, Opel, Mazda"
result1 = ["Bmw","Mercedes","Opel","Mazda"]
# 2- How many element list has?
print(len(result1))
# 3- What is first and last element?
print(f"First : {result1[0]} Last : {result1[-1]}")
# 4- Change 'Mazda' with 'Toyota'
result1[3] = "Toyota"
print(result1)
# 5- What element is at -2nd index?
print(result1[-2])
# 6- Is "Mercedes" element of list?
result2 = 'Mercedes' in result1
print(result2)
# 7- Take first 3 element of list
print(result1[:3])
# 8- Put "Toyota" and "Renault" instead last 2 elements of list
result1[-1] = "Toyota"
result1[-2] = "Renault"
print(result1)
# 9- Add to list "Audi" "Nissan"
result1 = result1 + ["Audi" , "Nissan"]
print(result1)
# 10- Delete last element of list
result1.remove('Nissan')  # -> alternative del result[-1]
print(result1)
# 11- Reverse and rewrite list
print(result1[::-1])
# 12- Make a list with datas given below
        #  studentA: Emre Uslu 2020, (70,60,70)
studentA = ["Emre","Uslu",2020,[70,60,70]]
        #  studentB: Seyma Gocer 2010, (80,80,70)
studentB = ["Seyma","Gocer",2010,[80,80,70]]
        #  studentC: Tolunay Uslu 1998, (80,70,90)
studentC = ["Tolunay","Uslu",1998,[80,70,90]]

# 13- Print elements
allstudents = studentA + studentB + studentC
print(allstudents) 

#### list methods

numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

min(numbers)  # -> 1
max(numbers)  # -> 16
max(letters)  # -> y  -> alphabetic sort
min(letters)   # -> a  -> alphabetic sort

numbers[3:6]  # 16 4 9

numbers.append(49)   # add a element to list
numbers.insert(3,78) # inserting 78 number to 3th index
numbers.insert(-1,52) # inserting 52 to -1st index
numbers.pop(1)        # deleting element on 1st index
numbers.remove(49)    # deleting "49" element
numbers.sort()        # sorting
letters.sort()        # sorting alphabetical
numbers.reverse()      # reversing list 
numbers.count(10)      # counting 10 on list
numbers.clear()        # clearing all elements on list
print(numbers)


####  list examples

names = ['Emre','Şeyma','Ender','Hale']
years = [1996,1995,2000,2010]

# 1- Add to end of list 'Tolunay'
names.append('Tolunay')
# 2- Add to beginning of list 'Dolunay'
names.insert(0,'Dolunay')
# 3- Delete 'Hale' frorm list
names.remove('Hale')
# 4- What is Hale's index?
names.index('Hale')
# 5- Is Emre in list?
print('Emre' in names)
# 6- Reverse list
names.reverse()
# 7- Sort names list alphabetical
names.sort()
# 8- Sort years list
years.sort()
# 9- str = "Chevrolet,Dacia" convert to list
string = "Chevrolet,Dacia"
string.split(',')
# 10- What is the biggest and smallest element of years list?
max(years)
min(years)
# 11- How many 2010 in years?
years.count(2010)
# 12- Delete all elements in years
years.clear()
# 13- Make a list with 3 elements that you receive from user
listem = []
for i in range(0,3):
        i = input('Give me a number user:\n')
        listem.append(i)
print(f"Your list:{listem}")



