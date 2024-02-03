student_count  = 1000 #naming convention in python with underline for seperating between words
rating = 4.99
is_published = False
course_name = """Multiple 
lines"""
# we can use signle qoat or double coat or multiline string as above
print(course_name)

x, y = 1, 2
z = w = 4
print(x,y)
#two typs of string formatting:
print("x={x},y={y}".format(x=x,y=y))#this is newer and is recommended in python 3
print("z=%(z)s , w=%(w)s" %{"z":z, "w":w})
#formatted string(this type of formatting works from python 3.6+):
first_name = "Arash"
last_name = "Karampour"
full_name = f"{first_name} {last_name} {len(first_name)} {2+5}" 
print(full_name)

# https://realpython.com/python-string-formatting/
# https://www.w3schools.com/python/ref_string_format.asp



#Python is a dynamic typing language! it means we can change the variable type and it's type can be changed during the run time!
# with type annotation and mypy linter we can become aware of type change in our code
#type annotation:
age: int = 25
#age = 'Python'
print(age)

#till 8 > continue from 8

#Some string methods:
course = "  Python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())#deleting white space at the beginning or end of the string(we have also rstrip and lstrip)
print(course.find("pro"))
print(course.replace("p","_"))
print("programming" in course)

print(course.lower().replace('p','_'))


#Numbers:
x = 10
x = 0b10 #binary form
print(bin(x))

x = 0x12c #hexadecimal format
print(hex(x))

x = 1 + 2j #complex form
print(x)

#Arithmetic OP

#+
#-
#*
print(10/3)
print(10//3) #integer division
print(10**3) #power
x = x + 1
x += 1
#we don't have x++ or x-- in python

#import math


# difference between is and == or is not and !=:
# is also checks for type equality but == just checks for value equality
#note: just use is for None or bool:
x = None
if x is None:
    print("x",x)

#12 Type Conversion:
x = input("x: ") # the result of input from user is always a string and for calculation we should convert it to proper type(that's why python is strongly typed language) but for examample in javascript it will be converted to a type implicitly(weakly typed language)
y = int(x) + 1 
print(y)
#int()
#float()
#bool()
#str()
"""
Falsy values:
1-""
2-0
3-[]
4-None 
"""

#13- conditional statments:
x = 3
if x > 2:
    pass # we use pass keyword just as a empty block for if statement because we don't hava empty block in python instead we use pass
else:
    print("ok")


#14- logical operators:
# and
# or 
# not
name = " "
if not name.strip():
    print('name is empty')

age = 25

if 18 <= age < 50:# this type of condition is valid in python like in math(instead we can also use with and logical operator)
    print("Eligible")