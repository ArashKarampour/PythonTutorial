# a module is a file that has related calsses , functions etc. 

def calc_tax():
    pass

def calc_shipping():
    pass


#6- intra-package reference here:
#1- first approach: absolute import: first the name of the top level package and then the package we want and then import the module you want
import sys
import os
#this below code is necessary if we want that the import below works when we run the sales3.py directly:
# in fact we are adding the directory of 6-modules to the sys.path, so that when we want to load a module it will also searches the directory of 6-modules and see the ecommerece package there
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# print(os.path.abspath(__file__)) # prints the absoloute path to the current module
# print(os.path.dirname(os.path.abspath(__file__))) # this prints the directory of the module

from ecommerce.customerPkg import contact

contact.contact_customer()


#2- second approache: relative import: . the current package and .. the previous(top level package)
# see this: https://chatgpt.com/share/9bf75289-6d42-410b-925a-f67e9e44d692
# from ..customerPkg import contact

# contact.contact_customer()


print('initializing the shoppingPkg with the sales3 module, __name__ :', __name__)