# 1- Lists:

# letters = ['a','b','c']
# zeros = [0] * 5 # this will repeat the item in the list for 100 times
# print(zeros)
# combined = zeros + letters # lists in python don't have to be the same type
# print(combined)

# numbers = list(range(20)) # list convert any iterable object into a list
# print(numbers)
# chars = list("Hello world")
# print(chars, len(chars))

# 2 accessing items:

# letters = ['a','b','c','d','e']
# print(letters[0:-2])
# print(letters[::-1]) # this will reverse the list
# print(letters[::-2]) # with negativ steps in fact we start from the end of the list with the poitive normal step numbers

# 3- unpacking lists:

# numbers = [1, 2, 3, 4, 5, 6]

# first, second, *other = numbers # this here called list unpacking. note that the number of variables on the left side should be equal to the number of list items or we can use this * to get other items(or packing the other list items)
# print(first, second)
# print(other)

# # first, second = numbers[0:2] # we can also unpack list with slicing
# first, *other, last = numbers
# print(first, last)
# print(other)

# 4- looping over lists:
# letters = ['a','b','c','d','e']

# for letter in letters:
#     print(letter)

# looping using enumerate built-in function
# for l in enumerate(letters):
#     print(l)

# for index,letter in enumerate(letters):
#     print(index,letter)

# 5- adding or removing items:

# #Add:
# letters = ['a','b','c']
# letters.append('d') #adding item at the end of a list
# letters.insert(1,'-') # adding an item in a specific location
# print(letters)

# #Remove:
# letters.pop(1) # removes the item with the index. by default it's last item in the list in others words index is -1
# letters.remove('b') # this will remove the first occurance item here for example first b in the list(for removing all b we must iterate the whole list and remove each b for example)
# del letters[0:2] # with del we can delete a range of items in a list
# letters.clear() # this will remove all the items in a list
# print(letters)

# # 6- finding items
# letters = ['a','b','c','a']
# if "d" in letters:
#     print(letters.index("d")) # if "d" is not in the letters we get an value error. therefore we first checked if there is a "d" in letters and then getting the index of it.
# print(letters.index("b"))
# print(letters.count('a')) # numbers of occurance of an item in a list

# 7- sortings lists:
# nums = [3, 51, 2, 8, 6]

# nums.sort() # this sort method modifies the nums array itself
# nums.sort(reverse=True)
# print(nums)

# string = "bbmkmkjkljlaaf"
# sortedstr = sorted(string)
# print(sortedstr)

# this is a built-in fucntion that we can pass an iterable to sort. it give us a (copy) list of the iterable and doesn't modify itself:
# sortedNums = sorted(nums, reverse=True)
# print(sortedNums)

# sorting the complex items:

# items = [
#     ("Product1",10),
#     ("Product2",9),
#     ("Product3",12),
    
# ]

# #sorting based on the price
# def sort_item(item):
#     return item[1]

# #items.sort(key=sort_item) 
# print(sorted(items,key=sort_item))
# print(items)

# 8- lambda (anonymous functions):

# items = [
#     ("Product1",10),
#     ("Product2",9),
#     ("Product3",12),
    
# ]
# # using lambda as an anonymous function to sort based on the price of the products in the list:
# # syntax: lambda parameters:expression(only one expression)
# # see: https://www.w3schools.com/python/python_lambda.asp for more examples
# items.sort(key= lambda item:item[1])
# print(items)

# 9- map function (map means transforming from one shape to another shape):

# items = [
#     ("Product1",10),
#     ("Product2",9),
#     ("Product3",12),   
# ]

# mapObject = map(lambda item:item[1], items) # this map function take a function and an iterable and appkyes the function on the itmes of the iterable(for exanmple a list here). it return a map object, which is itself also an iterable
# # we can convert it to a list using the list() built-in function:
# print(list(mapObject))

# # we could also iterate on the mapObject and reach it's items
# # for i in mapObject:
# #     print(i)

# # an important note about the map iterator object: we can only use this map iterator object one time to iterate or convert it. the second time it will be empty!!!

# 10- filter function:

# items = [
#     ("Product1",10),
#     ("Product2",9),
#     ("Product3",12),   
# ]

# filterObject = filter(lambda item: item[1] >= 10, items)
# # it's syntax is just like map function. it takes a function and an iterable(here items as a list). it loops through all the items of the iterable and if the criteria of the function is met then it returns that whole item.
# print(list(filterObject))
# # an important note about the filter iterator object: we can only use this filter iterator object one time to iterate or convert it. the second time it will be empty!!!(same as map object)

# 11- List Comprehension
# items = [
#     ("Product1",10),
#     ("Product2",9),
#     ("Product3",12),   
# ]

# #map with List Comprehension:
# prices = [item[1] for item in items]
# print(prices)

# # filter with list comprehension
# filtered = [item for item in items if item[1] >= 10]
# print(filtered) 

# 12- 
#https://www.w3schools.com/python/ref_func_zip.asp

# list1 = [1,2,3]
# list2 = [10,20, 30]

# print(list(zip('abc',list1,list2)))

# print(list(zip('abcdef',range(3),range(4))))

# 13- Stacks (LIFO):
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# last = browsing_session.pop()
# print(browsing_session)
# print("redirect", browsing_session[-1])
# if not browsing_session: # check if browsing_session is empty(list) : falsy values: 0, "", empty list, empty tuple,...
#     print("disable back button")

# 14- Queues:
# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")

# 15- Tuples : it's kind of read-only list
# point = 1,2 # or point = (1,2) , 1, , ()
# print(type(point))

# p = [1,2] + [3,4]
# point = (1,2) + (3,4)
# print(point)
# print(p)

# p = [1,2] * 3
# print(p)
# point = (1,2) * 3
# print(point)

# point = tuple("hello world")
# print(point)
# print(point[0:2])

# if "w" in point:
#     print('exists')

# x,y,*z = point
# print(x,y,z)

# 16- swapping variables:
# x = 10
# y = 11

# a,b = 1,2
# # swapping:
# x,y = y,x

# print(x,y)

# 17- Arrays: for larg list of numbers for better performance 
# from array import array

# # see: https://docs.python.org/3/library/array.html

# numbers = array('i', [4,3,2])
# numbers.pop()
# numbers.append(10)
# print(numbers)
# print(numbers[-1])
# strings = array('u',['a','b','c'])
# print(strings)
# print(strings[0])
# strings.append('d')
# print(strings)

# 18- Sets: collection with no dupplication: it's unordered collection
# numbers = [1,2,3,3,4]
# uniques = set(numbers)
# print(uniques)
# first = uniques

# second = {1,4}
# second.add(5)
# second.remove(1)
# print(second)

# print(first | second) # union on sets
# print(first & second) # intersection on sets
# print(first - second) # difference between first and second: items that are not in second but in first
# print(first ^ second) # symetric difference : items that are not in both

# #   print(first[0]) # we get an error because sets are unordered collection of unique items
# if 4 in first:
#     print('yes')

# 19- Dictionary
# Two different ways for difining a dictionary:
# point = {'x' : 1 , 'y': 2} # only immutable types for keys and anything for values
# point = dict(x=1,y=2) # key=word argument

# point['x'] = 10
# point['z'] = 20 # adding new key-value in dic
# print(point['x'])
# print(point)

# if 'a' in point:
#     print(point['a'])

# print(point.get('a')) # if a is not in the keys we get None with get method
# print(point.get('a',40)) # if a is not in the keys we can get a default value for it with this get method

# # deleting a key-value item from dic
# del point['x']
# print(point)

# # looping over dics:
# for key in point:
#     print(key, point[key])

# print("",end="\n\n")

# for x in point.items():
#     print(x)
#     key,value = x # unpacking the x in key and value
#     print(key, value)

# print("",end="\n\n")

# for key,value in point.items():
#     print(key ,value)

# print("",end="\n\n")

# print(point.items())
# print(point.keys())
# print(point.values())

# 20- Dictionary Comprehension:
# important: see video 20

# values = []
# # for x in range(5):
# #     values.append(x*2)
# # implementing the same code above with list comprehension:
# values_list = [x*2 for x in range(5)]
# print(values_list)
# # we can also use these kind of comprehension with sets (and also dictionaries):
# values_set = {x*2 for x in range(5)} 
# print(values_set)

# # comprehension with dictionaries:
# values_dict = {x:x*2 for x in range(5)} # x is key and x*2 is the value
# print(values_dict)

# 21- Generator Objects: we use generator for producing many numbers that won't take the memory like lists and are faster. it's iterable like list and in each iteration they generate a new value
# from sys import getsizeof

# values_list = [x*2 for x in range(20)]
# values_gen = (x*2 for x in range(20)) #  creating a generator object with generator expression
# print("genSizeINBytes", getsizeof(values_gen))
# print("listSizeINBytes", getsizeof(values_list))
# # we can not get the total length of generator because it won't save all the items in the memory and we just have access to the items during the run time
# print(values_gen)
# for x in values_gen:
#     print(x)

# 22 - Unpacking Operator * almost like ... in javascript: we can use unpacking operator * on any iterable
# numbers = [1,2,3]
# print(numbers)
# print(*numbers)

# # values = [*range(5)] # unpacking range and save it's values in a list
# # print(values)

# # we can also unpack strings (because it's also iterable)
# values = [*range(5), *'Hello']
# print(values)

# first = [1,2,3]
# second = [4,5,6]
# vals = [*first, *second] # combining two lists
# print(vals)

# # for unpacking dictionaries we need **
# first = {'x' : 1}
# second = {'x' : 10, 'y' : 2}
# vals = {**first, **second, 'z' : 1} # if we have the same key like x the last one we'll be saved(therefore x from second)
# print(vals)