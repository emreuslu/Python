#### tuples
# tuple object does not support item assignment!
# you can only use index and count methods in tuples
# you can not change anything after you created tuple


list = [1,2,3]
tuple = (1,'two',3)


#### dictionaries
# key - value
# 34 -> istanbul     06 -> ankara

cities = ['ankara','istanbul']
tags = [6,34]

tags = {'ankara' : 6,
        'istanbul' : 34}

tags['konya'] = 42

users = {'emreuslu' : {
        'age' : 24,
        'roles' : ['admin','roles'],
        'email' : 'eeuslu06@gmail.com',
        'phone' : 'XXXXXXXXXXXX'
        },
        'serkantoraman' : 26,
        'email' : 'serkantoramann3@windowslive.com',
        'phone' : 'XXXXXXXXXXXX'
        }

print(users['emreuslu']['roles'])     #  -> ['admin', 'roles']

#### dictionaries examples
# create a dictionary 'users' and fill the dictionary with inputs

students = { }
studentID = input('Student ID ? ')
studentName = input('Student name?')
studentSurname = input('Student surname?')
studentPhone = input('Student phone?')

# students = { studentID : {
#         'name' : studentName,
#         'surname' : studentSurname,
#         'phone' : studentPhone
# }}

students.update ( { studentID : {
        'name' : studentName,
        'surname' : studentSurname,
        'phone' : studentPhone
}})

studentID = input('Student ID ? ')
studentName = input('Student name?')
studentSurname = input('Student surname?')
studentPhone = input('Student phone?')

students.update ( { studentID : {
        'name' : studentName,
        'surname' : studentSurname,
        'phone' : studentPhone
}})

studentID = input('Student ID ? ')
studentName = input('Student name?')
studentSurname = input('Student surname?')
studentPhone = input('Student phone?')

students.update ( { studentID : {
        'name' : studentName,
        'surname' : studentSurname,
        'phone' : studentPhone
}})


print(students)
