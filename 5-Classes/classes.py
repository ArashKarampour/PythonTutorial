# 1- class is a blueprint for creating objects but object is an instance of the class


# 2- creating a class
# class Point: # using Passcal convention for naming in classes: each world with capital case
#     def draw(self): # all the methods should have at least a parameter called self
#         print("draw")


# # point = Point()
# # print(type(point))
# # print(isinstance(point, Point))
# # point.draw()

# 3- Constructor __init__:
# class Point: # using Passcal convention for naming in classes: each world with capital case
#     def __init__(self, x, y): # important: self is a reference to the current object
#         self.x = x # self.x is the field attribute of the object of class Point but x is the parameter to set it's value. we could also set self.x = defaultValue(a number for example)
#         self.y = y
#     def draw(self):
#         print(f"Point({self.x},{self.y})") # with self we can also access the field attributes or change them if necessary        


# #Recap:
# #1- use __init__ method as a constructor
# #2- self is the necessary parameter for each class method
# #3- we use self to create, access or change the field attributes of an object in a class
# point = Point(1,2)
# point.draw()

# 4- class vs Instance Attributes
# class Point: 
#     default_color = 'red' # it's a class level attribute and is shared between all objects of the calss

#     def __init__(self, x, y):
#         self.x = x        # attributes defined via self are instance attributes it means they're specific for each object but class level attributes are shared attributes among all objects of the class
#         self.y = y
#     def draw(self):
#         print(f"Point({self.x},{self.y})")       


# point = Point(1,2)
# point.z = 10 # we can create an instance attribute also outside of the calss(after creating an object) cause objects in python are dynamic
# point.draw()
# print(point.z)

# another = Point(3,4)
# another.draw()

# Point.default_color = "yellow"

# print(Point.default_color) # we can also use the class name to get access to class level attributes
# print(another.default_color)


# 5- Class vs Instance Methods:
# class Point:     
#     def __init__(self, x, y):
#         self.x = x    
#         self.y = y

#     @classmethod
#     def zero(cls): # here we've defined a classmethod using @classmethod and cls is a reference to the calss(here Point). we can call anything instead of cls
#         return cls(0,0) # same as Point(0,0) but with cls at runtime the method zero will pass the class reference to this cls parameter that we've defined as first parameter of this classmethod 
    
#     def draw(self):
#         print(f"Point({self.x},{self.y})")       

# point = Point.zero() # calling a class method using the classname
# point.draw()

# 6- magic methods: methods that have two underscore in the beginning and end of them and we can override them like : __init__ and __str__
# class Point:     
#     def __init__(self, x, y):
#         self.x = x    
#         self.y = y     
    
#     def __str__(self):
#         return f"({self.x},{self.y})"

#     def draw(self):
#         print(f"Point({self.x},{self.y})")       

# point = Point(1,2) # calling a class method using the classname
# st = str(point) # using the __str__ method implicitly for the object
# print(point) # using the __str__ method implicitly for the object
# print(st)

# 7- comparing objects : using magic methods: see also :https://realpython.com/python-magic-methods/#comparison-operator-methods
# class Point:     
#     def __init__(self, x, y):
#         self.x = x    
#         self.y = y     
    
#     def __str__(self):
#         return f"({self.x},{self.y})"
    
#     def __eq__(self, other): # __ne__ will implicitly be implemented by pythond after implementing(overrifing) this __eq__
#         return self.x == other.x and self.y == other.y
    
#     def __gt__(self, other): # __lt__ will implicitly be implemented by pythond after implementing(overrifing) this __gt__ 
#         return self.x > other.x and self.y > other.y

#     def draw(self):
#         print(f"Point({self.x},{self.y})")       

# point = Point(10,20)
# p2 = Point(10,20)
# another = Point(1,2)
# print(point == p2)
# print(p2 != another)
# print(point > another)
# print(point < another)

# 8- Performing arithmetic Operations: with arithmetic operator
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"({self.x},{self.y})"
    
#     def __add__(self,other): # this is the arithmetic operator for +.(to add two objects we define the behaviour here): it's like operator overloading in c++
#         return Point(self.x + other.x, self.y + other.y)
    
#     def __sub__(self,other): # this is the arithmetic operator for -.(to add two objects we define the behaviour here): it's like operator overloading in c++
#         return Point(self.x - other.x, self.y - other.y)

# point1 = Point(1,2)
# point2 = Point(3,4)
# point = point1 + point2 # the __add__ will be executed here when we want to add two objects together
# print(point)
# print(point2 - point1) # the __sub__ will be executed here when we want to add two objects together

# 9- Making custom Containers(datastructures):(video important)
#see also: https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/
# class TagCloud:
#     def __init__(self):
#         self.tags = {}
#     # here we delete the case sensitivity problem of typical dictionaries with our custom change
#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
#     # __getitem__ magic method for accessing objects like objectInstance[index] in array or objectInstance[key] in dictionaries this kind of calling on objects will invoke this magic method
#     def __getitem__(self, tag): 
#         return self.tags.get(tag.lower(), 0)
#     # with __setitem__ magic method we can set values like this on objects: objectInstance[index] = value or objectInstance[key] = value
#     def __setitem__(self,tag,count):
#         self.tags[tag.lower()] = count
#     # this __len__ magic method will be invoked when we call len(objectInstance)
#     def __len__(self):
#         return len(self.tags)
#     # __iter__ magic method works when we want to iterate over an object: note we should return with iter() function
#     def __iter__(self):
#         return iter(self.tags)
# cloud = TagCloud()
# cloud.add("python")
# cloud.add("Python")
# cloud.add("python")
# print(cloud.tags)
# print(cloud["python"]) # __getitem__ magic method will be invoked because of this line
# cloud["python"] = 10 # __setitem__ magic method will be invoked because of this line
# print(cloud["python"]) 

# print(len(cloud)) # this line will invoke the __len__ magic method

# for tag in cloud: # the __iter__ magic method will be called here when we want to iterate over cloud object
#     print(tag)