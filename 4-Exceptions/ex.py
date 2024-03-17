#1- Exceptions:  Exception is a kind of error that prevent our programm from running.
# numbers = [1,2]
# print(numbers[3]) # here we get an out of index exception
# age = int(input("Age: ")) # we get an ValueError exception if we input a character instead of a number


# 2- Handling Exceptions:

# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't enter the valid age!")
#     print(ex)
#     print(type(ex))
# else: # this only will be executed if we get no exception
#     print("No exceptions were thrown")

# print("Execution continues ...")

# 3- Handling different Exceptions:
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter the valid age!")
# else: # this only will be executed if we get no exception
#     print("No exceptions were thrown")

# print("Execution continues ...")

# 4-Cleaning up (continue of handling different exceptions):

# file = None
# try: #Note: if an exception occurs the rest of the code in try block won't be executed!
#     # some code ...
#     file = open("/home/arash/vscodeProjects/Python(mosh)/1-app1.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age     
# except Exception as ex: # we use this Exception as a generall Error handling
#     print(ex)
# finally:# for closing any kind of connections or files etc.
#     if file: # we check if file is opend at all and if it's defined (not None)
#         file.close()
#     print("finally this will be executed")

# 5- with statement:
# for opening file see: https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python

# with opening files using "with" we won't need any finally statement because "with" will automaticaly close the file after working with file is finished.
# in fact "with" supports so called context management protocole(which has __exit__ and __enter__ methods)
# we can also open multipe files within a with statement
# try:
#     with open("test.txt") as myfile, open("another.txt") as target:
#         print('file opend successfully')
# except Exception as ex:
#     print(ex)

# 6- Raising Exceptions:
# def calculate_xfactor(age):
#     if(age <= 0):
#         raise ValueError("Age can not be less than or equal 0")
#     return 10 / age

# try:
#     calculate_xfactor(0)
# except ValueError as err:
#     print(err)

# 7- Exceptions could be costly for huge amount of users(more than 10000 for example):
# from timeit import timeit #function to calculate the execution time of a python code

# code1= '''
# def calculate_xfactor(age):
#     if(age <= 0):
#         raise ValueError("Age can not be less than or equal 0")
#     return 10 / age

# try:
#     calculate_xfactor(0)
# except ValueError as err:
#     pass
# '''

# code2= '''
# def calculate_xfactor(age):
#     if(age <= 0):
#         return None
#     return 10 / age


# if calculate_xfactor(0) == None:
#     pass

# '''


# print(timeit(code1,number=10000)) #execute code1 10000 times and return execution time
# print(timeit(code2,number=10000)) 

# # the difference would be almost 1.5-2 times faster without raise exception and huge number of users
