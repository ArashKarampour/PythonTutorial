#1 creating modules:
# 1- first approach: from name_of_module import ...
from sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()

# 1.1
#from sales import * # if we just use * it will load all the functions or varables with the same name will be overwritten in this module

# 2- second approach
import sales

sales.calc_tax()
sales.calc_shipping()
#2 compiled python files:
# note: python only creates the compiled version of modules in the __pycache that we load but the main python file that we run will be compiled every time when we run the programm so we won't get a compiled version of that.


#3- Module search path
import sys
# this will print all the path that python searches for finding our libraries when we load them
# the first path is the current folder and then the pathes that python is installed with the packages etc.
# print(sys.path)


#4- Packages: loading the python modules from a folder

# import name-of-package.name-of-module
#1- first approach
import ecommerce.sales2
#very important: python cannot find the sales2 module so we have to add __init__.py  in the package folder so that python treat the folder as a package
#package is a container for one or more modules
# package is like a directory and module like a file in the filesystem
ecommerce.sales2.calc_shipping()

#2- second approach
from ecommerce.sales2 import calc_tax, calc_shipping

calc_tax()

#3- third and better approach
from ecommerce import sales2
sales2.calc_tax()


#5- loading modules from sub pakcages
from ecommerce.shoppingPkg import sales3
sales3.calc_tax()

#6 intra-Package references: loading a module from a sibling package: see sales3.py in shoppingPkg : this just works if we load that sales3.py from the app.py that is in the directory that ecommerce is in it, so that the sales3.py will see the ecommerce when we load it form app.py

#7 dir built-in function: to get the list of all attributes and methods defeined in an object
# print(dir(sales3))
# print(sales3.__name__) # name of the module with it's package name
# print(sales3.__package__) # name of the package(s), in which the the module is
# print(sales3.__file__) # path to the file of the module
# print(__name__)
# print(__package__)
# print(__file__)

#8- executing modules as scripts:
# if we write anything like print statments only the first time that the module is loaded it will be executed it's also true for packages(if we add something in __init__.py for example): if we load the module again in the same execution it won't be executed
# this code below will check if we run our module directly and as the main module it will be exectued but if we load this module in another app this won't be executed
if __name__ == '__main__':
    print('yes')

