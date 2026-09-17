#this is my first program

# print ("I like pizza!")
# print("fuck you")

#variables = a container of a value (string, integer, float, boolean)
#            a variables behaves as if it was the values it contains

#strings
# first_name = "Mohit" 
# food = "biryani"
# email = "fuckyou@fake.com"

#print (first_name)

#f-string represent format
# print (f"this is my fav {food}")
# print (f"my email {email}")

# few usefull string method
# name = input("Enter your full name: ")
# result = len(name)
# result = name.find("z")
# result = name.rfind("m")
# result = name.isdigit()
# result = name.isalpha()
# result = name.count("o")
#  result = name.replace("o", " ") error


# print(result)
# name = name.capitalize()
# name = name.upper()
# name = name.lower()

# print(name)

#integer

# age = 19
# quantity = 3
# num_of_students = 30

# print ("your age is" ,age)
# print (f"your  age is :{age} ")
# print (f"you are buying {quantity} items")
# print (f"your class has :{num_of_students} students")

# float

# price = 10.99
# gpa = 8.07
# distance = 5.55

# print (f"the item costs {price} dollars")
# print (f"this is my {gpa} of this year")
# print (f"i ran {distance}km today")

# boolean (it is used to define the statement is true or false)

# is_student = True
# is_forsale = False
# is_online = True

# if is_student:
#     print("he is a student ")
# else:
#     print("not a student ")

# if is_forsale:
#     print("available")
# else:
#     print("not available")

# if is_online:
#     print("he is a online ")
# else:
#     print("he is offline ")

# typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()
 
# name = "luffy"
# age = 19
# bounty = 100000000.00
# pirate_king = True


# converting them

# age = float(age)
# bounty = int(bounty)
# pirate_king = str(pirate_king)
# name = bool(name)


# print(type(name))
# print(type(age))
# print(type(bounty))
# print(type(pirate_king))




# input() = A functions that prompts the user to entier data 
#           returns a entered data as a string

# name = input("what is your name? ")
# age = int(input("how old are you?:"))

# # age = int(age)
# age = age+1

# print(f"hello {name}!")
# print("happy birthday")
# print (f"now you are {age} years old")



# arithmatic operations
# math operation

# pizza = 10
# # pizza = pizza+1
# # pizza *= 2
# # pizza /= 5
# # pizza **= 2
# pizza %= 3
# print(pizza)

# x = 3.14
# y = 4
# z = 5

# result = round(x)
# final = abs (y)
# power = pow(2,3)
# heigest_value = max(x,y,z)
# lowest_value = min(x,y,z)

# print(result)
# print(final)
# print(power)
# print (heigest_value)
# print(lowest_value)

# import math

# print(math.pi)
# print(math.e)
# # result = math.sqrt(9)
# # result = math.ceil(3.1)
# result= math.floor(9.9)
# print(result)

# if = do some code only if some condition is True
#     else do something else
 
# age = int(input("enter your age :"))
# if age>=100:
#     print("you are too old to vote")
# elif age>=18:
#     print("you can vote")
# elif age<0:
#     print("your are not born yet")

# else:
#     print("you can't vote")

# response = input("would you like to have some food (Y/N):")
# if response == "Y":
#     print("what would you like to have ")
# else:
#     print("why")

# name = input("Enter your name: ")
# if name == "":
#     print("entre your name bitch")
# else:
#     print(f"hello {name}!!!")

# is_student = True
# is_forsale = False
# is_online = True

# if is_student:
#     print("he is a student ")
# else:
#     print("not a student ")

# if is_forsale:
#     print("available")
# else:
#     print("not available")

# if is_online:
#     print("he is a online ")
# else:
#     print("he is offline ")

# logical operator = evaluate multiple conditions (or, and, not)
#                    or = atleaast one condition should be true 
#                    and = both condition must be true
#                    not = inverts the condition (not true, not false)

# temp = int(input("enter the temp: "))
# is_rainnig = False

# if temp>35 or temp<0 or is_rainnig:
#     print("the event is cancelled")
# else:
#     print("the event is still scheduled")
 
# temp = 25
# is_sunny = False

# if temp<=30 and is_sunny:
#     print("you can go out to play")
# else:
#     print("you can't go out to play")

# conditional expression = A one-line shortcut for the if-else statement
#                          (ternary operator) print or assign one of two 
#                          values based on a condition X if condition else Y

# num = int(input("enter the number: "))
# print ("positive" if num > 0 else "negative")
# print("even" if num % 2 ==0 else "odd")
# age = num
# print("Adult" if age>=18 else "Minnor")
# user_role = input("enter the pass: ")
# user_access = print("full access" if user_role == "admin" "limited access"  else "no access")

# indexing = accessing elements of a sequence using [] (indexing operators
#            [start : end : step]                                          )
# credit_number = "1234-5678-9012-3456"
# print (credit_number[0])
# print (credit_number[0:4])
# print (credit_number[::2])
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 allocate and zero pad that many spaces
# :<= left justify
# :> = right justify
# ^=center align
# :+= use a plus sign to indicate positive value
# :== place sign to leftmost position
# : = insert a space before positive numbers
# ون = comma separator

# price1 = 259.365
# price2 = -3657.36987
# price3 = 23.658

# print(f"price 1 is ${price1:.2f}")
# print(f"price 2 is ${price2:.4f}")
# print(f"price 3 is ${price3:07}")

# while loop = execute some code while some condion remains true

# name = input("Enter your name: ")

# while name == "":
#     print ("naam daal dalle")
#     name = input("Enter your name: ")


# print(f"hello {name}")

# age = int(input("enter your age: "))
# while age < 0:
#     print("age can't be nagative")
#     age = int(input("enter your age: "))
# print(f"your age is {age} y/o")

# food = input("Enter a food you like (done to stop): ")
# while not food == "done":
#     print(f"you like {food}")
#     food = input("Enter another food you like: (done to stop): ")
# print("bye")

# num = int(input("enter an number between 1-10: "))
# while num > 10 or num<1:
#     print("the input is incorrect")
#     num = int(input("enter an number between 1-10: "))
# print("bye")

# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.

# credit_card = "1234-5678-9012-3456"
# name = input("enter your name: ")
# for x in range(1, 21):
#     if x == 13:
#         continue
#     elif x == 17:
#        break
#     else:
#      print(x)
# print("happy birthday")

# nested loops = a loop within another loop (outer,inner)
#                outer loop:
#                    inner loop:

# for c in range (3):
#     for x in range(1,11):
#         print(x, end="")
#     print()


# collection = single "varaible" used to store multiple values
# list = [] ordered and changeable. duplicate ok
# sets = {} unordered and inmutable, but add/remove ok. not duplicates
# tuple = () ordered and unchangeable, duplicate ok faster



# list
# fruits = [ "apple", "mango", "banana", "orange"]
# fruits[0] = "pineapple"
# fruits.append("grapes")
# fruits.remove("mango")

# print(fruits[::2])
# for x in fruits:
#     print(x,end=" ")


# set
# fruits = { "apple", "mango", "banana", "orange"}
# fruits[0] = "pineapple"
# fruits.append("grapes")
# fruits.remove("mango")

# print(fruits[::2])
# for x in fruits:
    # print(x,end=" ")



# tuple
# fruits = ("apple", "mango", "banana", "orange")
# for x in fruits:
#     print(x,end=" ")

# 2D list collection

# fruits =      ["apple", "oranges", "banana", "grapes"]
# vegetables =  ["potato","pumpkin", "tomato", "chilly"]
# meats =       ["chicken", "mutton", "beef", "fish"]

# groceries = [fruits,vegetables,meats]

# print(groceries[2][2])


# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# capitals = {"USA":"Washington DC",
#             "India":"New Delhi",
#             "Russia":"Moscow",
#             "Spain":"Madrid"}

# if capitals.get("Spain"):
#     print("that capital does exist")
# else:
#     print("that capital doesn't exists")

# capitals.update({"Germany":"Berlin"})
# print(capitals.get("Germany"))
# capitals.pop("Russia")
# print(capitals)
 
# keys = capitals.keys()
# for key in keys:
#     print(key)

# values = capitals.values()
# for value in values:
#     print(value)



# import random

# number = random.randint(1,6)
# print(number)


# function = a block of reusable code 
#            place() after the function name to invoke it

# def happy_birthday(name,age):
#     print(f"happy birthday to {name}")
#     print(f"how old are {age}")
#     print("happy birthday to you")

# happy_birthday("lavdya",10)

# return = statement used to end a function
#          and send a result to the caller

# def add(x,y):
#     z = x+y
#     return z

# def substract(x,y):
#     z = x-y
#     return z

# def divide(x,y):
#     z = x/y
#     return z

# def multiply(x,y):
#     z = x*y
#     return z

# print(add(1,3))
# print(substract(1,3))
# print(multiply(1,3))
# print(divide(1,3))

# def create_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " "+ last

# full_name = create_name("mohit","bhosande")
# print(full_name)


# default arguments = a default value for certain parameters
#                     default is used when that argument is omitted
#                     make your function more flixible, reduces # of arguments
                    # 1.postional, 2.default, 3.keyword, 4.arbitrary


# def net_price(list_price,discount=0,tax=0.05):
#     return list_price * (1-discount) * (1+tax)
# print(net_price(500))

# keyword argument = an argument proceded by an identifier help with readability
#                    order of argument doesn't matter
                    # 1.postional, 2.default, 3.keyword, 4.arbitrary
                   
# def hello(greeting,title,first,last):
#     print(f"{greeting} {title}{first} {last}")

# hello("hello","mr.","walter","white")
# hello("hello",last="white",title="mr.",first="walter",)


# *args    = allows you to pass multiple non key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            unpacking operators
        # 1.postional, 2.default, 3.keyword, 4.arbitrary

# def add(x,y):
#     return x+y
# print(add(1,2))

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4))

# def name(*args):
#     for arg in args:
#         print(arg, end=" ")

# print(name("mohit","bhosande"))
# name("mohit","bhosande")

# def address(**kwargs):
#     for value in kwargs.values():
#         print(value)
# address(street= "hawa galli ",city= "chutadpur" ,state="lavdale" ,pin=416969)

# def address(**kwargs):
#     for key in kwargs.keys():
#         print(key)
# address(street= "hawa galli ",city= "chutadpur" ,state="lavdale" ,pin=416969)

# def address(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
# address(street= "hawa galli ",city= "chutadpur" 
#         ,state="lavdale" ,pin=416969)

# iterables = an object/collection that can return its elements one at a Time,
#             allowing it to be iterated over in a loop

# numbers = (1,2,3,4,5,)
# for num in numbers:
#     print(num) 
    # in this case "num" is iterables

# name = "bro Code"

# for char in name:
#     print(char,end="")


# membership operators = used to test whether a value or variable is 
#                        found in a sequence
#                        (string,list, tuple, set, or dictionary)


# word = "choot"
# letter = input("guess a letter in secert word: ")

# if letter in word:
#     print(f"{letter} is there")
# else:
#     print(f"{letter} is not there")

# if letter not in word:
#     print(f"{letter} is not there")
# else:
#     print(f"{letter} is there")

# list comprehension = a concine way to create a lists in python
#                      compact and easier to read than traditional loops
#                      [epression for value in iterable if condition]

doubles = [x*2 for x in range(1,11) ]
triples = [y*3 for y in range(1,11) ]
square = [z*z for z in range(1,21)  ]
print(square)

# numbers = [1,2,-3,-4,5,-6]
# positive_num = [num for num in numbers if num>=0]
# negative_num = [num for num in numbers if num<=0]
# even = [num for num in numbers if num % 2 == 0 and num>=0]
# odd = [num for num in numbers if num % 2 == 1 and num>=0]
# print(even)
# print(positive_num)
# print(negative_num)
# print(odd)

# match-case statement (switch): An alternative of using many 'elif' statement
#                               execute any code if the value matches a 'case'
#                               benifit: clear and syntax is more readable 

# def days_of_week(day):
#     match day:
#         case 1:
#                 return "it is sunday"
#         case 2:
#                     return "it is monday"
#         case 3:
#                     return "it is tuesday"
#         case 4:
#                     return "it is wednesday"
#         case 5:
#                     return "it is thursday"
#         case 6:
#                     return "it is friday"
#         case 7:
#                     return "it is saturday"
#         case _:
#                     return "not valid"

# print(days_of_week(1))



# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to breakup a large program reuseable seperate files
# import math
# print(help("modules"))

# print(help("math"))

# print(math.e)


# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> enclosed -> global -> built-in

# local varaible
# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)

# func1()
# func2()
                    
# global variable


# def func1():
     
#     print(a)

# def func2():
    
#     print(a)
# a =2        
# func2()-


# if __name__ == __main__: (this script can be imported OR standalone)
#                          function and class in this module can be reused
#                          without the main block of code executing


# object = a "bundle" of related attributes (variables) and method functions
#          Ex. phones, cup, book
#          you need a "class" to create many objects

# class = (blueprint) used to design the structuer and layout of an object