# 15 Ternary operator in python like ? :
'''
age = 25
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
'''
# 16- for loops
'''
for w in 'python':
    print(w)

for l in ['a','b',2]:
    print(l)

for i in range(0,10,2):
    print(i)
'''

# 17- for...else:
# this structure could be replaced with a found bool flag(see video 17): in fact if break doesn't execute at the end the else block will be executed
'''names = ["AJane","Tom"]

for name in names:
    if name.startswith("J"):
        print("found")
        break
else:
    print('not found')
'''
# 18- while loop: nothing special. we can also use while ...else here like for ...else

# 19- functions
'''
def increment(number: int, by: int = 1) -> tuple: #default value for by is 2 in this function. we can also use type annotation for arguments and also return type of the function
    return (number,number+by) # in python we can return two or more things(as a tuple by default even if we delete the parantheses)

print(increment(4,by=2)) # here by= is a keyword argument. we write like this for more readablity of code.
'''


# 20 arguments- *args :
'''
def multiply(*items):
    #print(items) #it will be a tuple
    total = 1
    for number in items:
        total *= number
    return total


print(multiply(2, 3, 4, 5, 6))
'''


# 21 arguments- **args
'''
def save_user(**user): #with this **args we can only pass keyword arguments and what we get is a dictionary as a result of **arg
    print(user)
    print(user['id'])
    print(user['name'])

save_user(id=1, name='admin') #just passing keyword arguments is valid for **args
'''

# 22- Scopes (important in my opinion):
'''
# local variables are in function scope
# global variables are in file scope
# we don't have block level variables in python like in javascript(variables in if conditions and loops are accessible outside of them in python unlike in javascript or other programmin languages)

message = 'a' # this is a global or filescope variable
message0 = 'c'

def greet():
    print('message0: ', message0)
    if True:
        message1 = 'a'
    print('message1:',message1)#this message1 is accessible outside of if conditon
    #global message # with this line we make our local message varaible access the global varibale outside of function in fact our local variable becomes the same global variable (it's not a good idea to do this in practice!)
    message = 'b' #this message is a local variable 
    print('message in function scope: ', message)

greet()
print('message: ',message)# when we use the same name variable in function the filescope variable will become invalid inside of function and only the functionscope variable is valid
'''

# 23 debuging in vscode
# 24 tricks in vscode
# 26-27 fizzBuzz exercise