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

# 10- private members:
# use self.__varName instead of self.varName for defining an attribute as a private one 
# we can also make a method private with adding just double underscore to the beginning of it
# class testClass:
#     def __init__(self):
#         self.__testVar = 20
#         self.testvar2 = 22
#     # this changevar is now a private method with this __ in the front of it.
#     def __changevar(self, value):
#         self.__testVar = value
    

# test = testClass()
# #print(test.__testVar) # here we get an AttributeError because this variable is kind of private(but actually can be still accessed!)
# print(test.__dict__) # every object or calss in python has the method __dict__, which holds all the attributes in the class
# print(test._testClass__testVar) # it just added the classname with _ to the name of the private variable
# # in fact with this kind of naming we are considering the convention for making the variables private and to warn that they must not be changed.

# 11- Properties : they're used to take control over the attribute set and get (for more details watch the vid)
# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0: # here is where we can control the value that is going to be set for price.
#             raise ValueError("Price cannot be negative!")
#         self.__price = value
    
# product = Product(10)
# product.price = 2
# print(product.price)

# # with @property decorator we made the price function as a property or attribute field(getter method)
# # with @price.setter we have defined the setter method for price attribute 
# # when we say self.price or product.price the getter method or the method with @property will be called
# # when we say self.price = value or product.price = value the setter method will be called
# # Note: we can not name the property field and the value we set for that the same because we'll get RecursionError (therefore here we set self.__price in the setter and not self.price)

# 12,13- Inheritance: it prevents code duplication and allows us to reuse code

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("can eat")
    
# class Bird(Animal):
#     def fly(self):
#         print("can fly")
    
# class Fish(Animal):
#     def swim(self):
#         print("can swim")


# b = Bird()
# b.eat()
# b.fly()
# print(b.age)

# # the subclass can inherite the both the methods and the attributes of the super class

# print(isinstance(b,Animal))
# print(isinstance(b,object)) # every class inherites from the object class

# 14- Method Overriding: replacing or extending a method defined in the base class 
# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("can eat")
    
# class Bird(Animal):
#     def __init__(self): # this __init__ method overrides the __init__ method in the base class
#         super().__init__() # with this super method we'll have access to any methods and attribute of the supercalls(without this line we couldn't have access to the age attribute defined in the super class)
#         self.weight = 2

#     def fly(self):        
#         print("can fly")


# b = Bird()
# print(b.weight)
# print(b.age)

# 15- Multi-level Inheritance:

# class Animal:
#     def eat(self):
#         print("can eat")
    
# class Bird(Animal):        
#     def fly(self):        
#         print("can fly")

# class Chicken(Bird): # but a chicken cannot fly(so try not to use such kind of inheritance)
#     pass

# # try to avoid multi level inheritance mostely. but if you want to use Inheritance just limit it to one or two levels

# 16- Multiple Inheritance:

# class Employee:
#     def greet(self):
#         print("Employee Greet")
    
# class Person:
#     def greet(self):
#         print("Person Greet")

# class Manager(Person,Employee): # the order of inheritance here is important for calling the greet method(the same method name)
#     pass

# manager = Manager()
# manager.greet() # this method will be called based on the fact, that which class we inherite from first()
# # if the original class has the method it will call it but if not it will call the method in the super class in the order of Inheritance we defiend(if we have a multiple inheritance)

# # this here could be a good example of multiple inheritance:
# class Flyer:
#     def fly(self):
#         pass

# class Swimmer:
#     def swim(self):
#         pass

# class FlyingFish(Flyer, Swimmer):
#     pass

# 17- a good example of Inheritance:

# # Custome exception:
# class InvalidOperationError(Exception):
#     pass


# class Stream:
#     def __init__(self):
#         self.openned = False

#     def open(self):
#         if self.openned:
#             raise InvalidOperationError("Stream is already open!")
#         self.openned = True
    
#     def close(self):
#         if not self.openned:
#             raise InvalidOperationError("Stream is already close!")
#         self.openned = False


# class FileStream(Stream):
#     def read(self):
#         print("reading data from a file")
    

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# n = NetworkStream()
# n.close()

# 18- Abstract Base Classes: the Stream class from example video 17 has two issues:

# 1- we shouldn't be able to direcltly creat an instance of Stream class(it should be a abstract class)
# 2- the read method should become an abstract method that other sub classes must implement it

# this line is important for making a abstract class and method:
# from abc import ABC, abstractmethod
# # from abc module we import ABC class (Abstract Base Class) and abstractmethod as a decorator method

# # Custome exception:
# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.openned = False

#     def open(self):
#         if self.openned:
#             raise InvalidOperationError("Stream is already open!")
#         self.openned = True
    
#     def close(self):
#         if not self.openned:
#             raise InvalidOperationError("Stream is already close!")
#         self.openned = False

# # defining the read as an abstract method:
#     @abstractmethod
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         print("reading data from a file")
    

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a memory stream")

# # s = Stream() # we cannot instantiate the abstract class Stream here 

# m = MemoryStream()
# m.read()

# 19- Polymorphism: when we have different classes that inherite from the same class and they
# implement one or many (abstract)methods of the base class and based on these implementation
# and that we use which object of which class we will get different results at runtime because
# of this different implementation of the abstract methods of the base class

# 20- Duck Typing: if it walks like a duck and quaks like a duck it is a duck!
# it means the python just looks for the existence of a method and not the type of the objects
# that call that method, since python is a dynamicly typed language
# it means to achieve polymorphism behaviour we don't have to have a base calss and inheritance
# but with that all having a base class is still a good practice


# # 21- extending the built-in clasees:
# class Text(str):
#     def duplicate(self):
#         return self + self


# mystr = Text("this is my str")
# m = mystr.duplicate()
# print(m)

# class TrackableList(list):
#     def append(self,obj): # actually here we are overriding the append method of the list class(type)
#         print('append called')
#         super().append(obj)

# l = TrackableList()
# l.append('12')
# print(l)

# # 22- Data classes (namedtuple classes): # it's used when we work with data and no methods and they have attributes when we want to create an instance of them and we can not modify them after they are created. they also have magic methods by default
# # see also: https://www.geeksforgeeks.org/namedtuple-in-python/

# from collections import namedtuple

# Point = namedtuple('Point',['x','y'])

# p1 = Point(x=2,y=3)
# p2 = Point(2,3)
# p3 = Point(2,4)

# print(p1.x)
# print(p1[1])

# print(p1 == p2)
# print(p1 < p3)