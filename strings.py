##### string formatting

result = 200/700
print('The result is {}\n'.format(result))  # -> output : The result is 0.2857142857142857
print('The result is {r}\n'.format(r=result))  # -> output : The result is 0.2857142857142857
print('The result is {r:1.3}\n'.format(r=result))   #->  output : The result is 0.286
print(f'The result is {result:1.3}\n')  # ->  output : The result is 0.286

##### string parsing

name = 'Emre Uslu 132'

print(name[2::2])  #  ->  output : r su12


#####  string formatting and parsing example

website = "http://www.github.com/emreuslu"
course = "Python Course: From Zero to Expert Python (40 Hours)"

# 1- How many characters in 'course' string?
print(len(course)) 
# 2- Take www chars from 'website'
print(website[7:10])
# 3- Take com chars from 'website'
print(website[18:21])
# 4- Take first and last 15 chars from 'course'
print(f'{course[:15]}, {course[-15:]}') 
# 5- Reverse and Rewrite 'course' string
print(f'{course[::-1]}')

name, surname, age, job = 'Emre', 'Uslu', 24, 'Engineer'

# 6- Print the sentences below using above variables
#    'My name is Emre Uslu, My age is 24 and I'm engineer.'

print(f"My name is {name} {surname}, My age is {age} and I'm {job}")

#7 - Change w wih W in 'Hello world'

sentence = 'Hello world'
print(sentence.replace('w','W'))

# 8- print 'abc' 3 times side by side
sentence = 'abc'
print(sentence*3)

#####  string methods

message = "Hello there. My name is Emre Uslu and I'm learning Python."

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()
# message = message.strip()
# message = message.split()
# message = message.split('.')
# message = '*'.join(message)
# index = message.find('Emre')
# isFound = message.startswith('E')   -> returns Boolean
# isFound = message.endswith('u')    -> returns Boolean
# message = message.replace(' ','*')   
# message = message.center(80,'*')    -> ***********Hello there. My name is Emre Uslu and I'm learning Python.*********** 

#####  string methods examples

website = "http://www.github.com/emreuslu"
course = "Python Course: From Zero to Expert Python (40 Hours)"

# 1- Delete first and last char in ' Hello World ' string
s = ' Hello World '
s = s.strip()
s = s[::-1]
s = s.strip()
s = s[::-1]
print(s)
# 2- Delete all characters except from emreuslu 'wwww.emreuslu.com'
s = "wwww.emreuslu.com"
s = s.strip('w.com')
print(s)
# 3- upper all chars in 'course' string
print(course.upper())
# 4- how many 'e' chars in 'website' string
print(website.count('e'))
# 5- Is website starts with 'www' and ends with 'com' ?
s = website.startswith('www')
print(s)
# 6- Is there any '.com' string inside 'website' ?
print(website.find('.com'))
print(website.rfind('.com'))
print(website.index('.com'))
print(website.rindex('.com'))
# 7- Is every char in 'course' alphabetical?
print(course.isalpha())
print(course.isdigit())
# 8- Put the 'Contents' string inside of 50 char and add *
print('Contents'.center(50,'*'))
print('Contents'.rjust(50))
# 9-  Replace ' ' with '-' in 'course
print(course.replace(' ','-'))
# 10- Replace 'World' with 'There' in 'Hello World'
print('Hello World'.replace('World','There'))
# 11- Split 'course' string ' '
print(course.split())
