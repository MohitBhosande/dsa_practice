# exercise 1 rectangle area calc

# lenght = float(input("enter the lenght:"))
# width = float(input("enter the width:"))

# area = lenght*width
# print (f"the area is {area}cm²")

# Exercise 2 shopping cart program

# item = input("what would you like to buy?: ")
# price = float(input("what is the price of item?: "))
# quantity = int(input("how many would you like?: "))
# total = price*quantity
# print(f"the amount you have to pay is ${total}")

# print(f"your amount in INR is {inr}rs and in dolllar is {dollar}bucks")


# print("thank you!")

# Exercise 3 
# Madlibs game
# word gamae where you create a story
# by filling in blanks with random words 

# adjective1 = input("Enter an place:")
# noun1 = input("enter a noun:")
# adjective2 = input("enter an emotion:")
# verb1 =input("enter a verb ending with 'ing':")
# # noun1 = input("enter a noun:")
# # adjective3 = input("enter an emotion:")


# print(f"today I went to a {adjective1}")
# print(f"there I saw a {noun1}")
# print(f"{noun1} was {adjective2} while {verb1}")
# print(f"{noun1} was {adjective2} when he won!!" )

# Exercise 4
# import math 
# Exercise calculate the circumference of circle

# radius = float(input("enter the radius:"))
# circumference = 2*math.pi*radius

# print(f"the circumference of the circle is : {circumference} ")

# Exercise area of a circle
# radius = float(input("enter the raadius:"))
# area = math.pi* pow(radius,2)
# print(f"the area of circle is {area}")

# exercise for pythagoras theorem
# a = float(input("enter the value of a:"))
# b = float(input("enter the value of b:"))
# c = pow(a,2)+pow(b,2)

# math.sqrt(c)
# print(f"hypotenus of a and b is {math.sqrt(c)}")

# python calculator
 
# operator = input("enter the operator you would like to use (+ - * /):")
# num1 = float(input("enter the integer: "))
# num2 = float(input("enter the integer: "))
# if operator == "+":
#     print(num1+num2) 
# elif operator == "-":
#     print(num1-num2)
# elif operator == "*":
#     print(num1*num2)
# elif operator == "/":
#     print(num1/num2)
# else:
#     print(f"{operator} is not a vaild opeator")

# python weight converter

# unit = input("killograms or pounds (K or P): ")
# weight = float(input("enter your weight: "))
# print (weight)


# if unit == "K":
#     weight = weight * 2.205
#     unit = "lbs"
#     print(f"your weight is {round(weight)} {unit}")
# elif unit == "P":
#     weight = weight * 0.453592
#     unit = "kg"
#     print(f"your weight is {round(weight)} {unit}")
# else:
#     print(f"{unit} is not a valid unit")

# temperature converter
# unit = input("enter the unit (C/F): ")
# temp = float(input("enter the temperature: "))

# if unit == "C":
#     temp = (9*temp)/5 + 32
#     unit = "fahrenheit"
#     print(f"the temp in fahrenheit is {temp} °F")
# elif unit == "F":
#     temp = (temp-32) * 5/9
#     unit = "celsius"
#     print(f"the temp is {temp} °C")
# else:
#     print(f"{temp} is not valid")

# Exercise (validate users input)
# 1. user name is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("enter the user name: ")
# result = len(username)
# space = username.find(" ")
# digits = username.isalpha()


# if len(username) >= 12:
#     print("your username can't be more than 12 character ")
# elif not username.find(" ") == -1:
#     print("your username can't be have space")
# elif not username.isalpha():
#     print("your username can't have digits")

# else:
#     print(f"welcome {username}")


# Python compound intrest calculator

# P = float(input("enter initial principle balance: "))
# while True:
#     P = float(input("Enter the principal amount: "))
#     if P < 0:
#         print("principal can't be zero: ")
#     else:
#       break

# while True:
#     R = float(input("enter the rate intrest: "))
    
#     if R < 0:
#         print("principal can't be zero: ")
#     else:
#         break

# # time = float(input("enter the time period elapsed: "))
# while True:
#     time = float(input("enter the time period elapsed:"))
#     if time < 0:
#         print("principal can't be zero: ")
#     else:
#         break

# A = P* pow((1 + R/100), time)
# print (f"compoud intrest is {A}")
# total = A+P
# print(f"the total amount you have now is {total}")

# import time


# my_time = int(input("enter the time you want to set: "))

# for x in range(my_time, 0,-1):
#     seconds = x % 60
#     minutes = int(x/60) % 60
#     hours = int(x/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
   
#     time.sleep(1)
#     print("happyy birthday")



# print ractange made with some symbol

# rows = int(input("enter the rows you want: "))
# coloumn = int(input("enter the coloumn you want: "))
# symbol = input("enter the symbol to use: ")

# for c in range (rows):
#     for x in range(coloumn):
#         print(symbol, end="")
#     print()

# shopping cart program

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("enter the food you want to buy (q to quit): ")
#     if food.lower() == "q" :
#         break
#     else:
#         price = float(input(f"enter the price of a {food} $"))
#         foods.append(food)
#         prices.append(price)

# print("-----your cart-----")

# for food in foods:
#     print(food,end=" ")

# for price in prices:
#     total += price
# print()
# print(f"your total bill is ${total}")


# concession stand program

# menu = {"pizza":"5.99",
#         "vadapav":"2.99",
#         "momo":"3.99",
#         "burger":"3.99"}

# cart = []
# total = 0

# for key, value in menu.items():
#     print(f"{key:10}: ${value}")  

# print("q to quit")
# while True:
#     food = input("select the food items from the menu: ").lower() 
#     if food == "q":
#             break
#     elif menu.get(food) is not None:
#          cart.append(food)

# for food in cart:
#     total = menu.get(food)
#     print(food, end=" ")

# # total = total + menu.get(food)

# print()
# print(f"your total is ${total}")
  

# number gussing game

# import random

# lowest = 1
# highest = 100
# guesses = 0
# answer = random.randint(lowest,highest)
# print(answer)
# is_running = True
# print("this is number guessin game")
# print("select a number between {lowest} and {highest}")
# while is_running:
#     guess = (input("enter the guess: "))

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess>highest or guess<lowest:
#             print("out of range")
#             print("select a number between {lowest} and {highest}")
#         elif guess>answer:
#             print("to high!!")
#         elif guess<answer:
#             print("too low!!")
#         else:
#             print(f"correct the ans was {answer}")
#             print(f"the number of guesses you took was {guesses}")
#             is_running = False
#     else:
#         print("invalid guess")
#         print("select a number between {lowest} and {highest}")
            
# import random

# option = ("paper","rock","sessiors")

# running = True

# while running:
#     player = None
#     computer = random.choice(option)

#     while player not in option:
#         player = input("enter the choice: ")

#     print(f"player: {player}")
#     print(f"computer: {computer}")

#     if player == computer:
#         print ("it's a tie!!")
#     elif player == "rock" and computer == "sessiors":
#         print("you won!!")
#     elif player == "sessiors" and computer == "paper":
#         print("you won!!")
#     elif player == "paper" and computer == "rock":
#         print("you won!!")
#     else:
#         print("you lose!!")
#     play_again = input("play again (y/n): ")

#     if not play_again == "y":
#         running = False

# print("thanks for playing!!")

# invoice 

# def display_invoice(username,amount,due_date):
#     print(f"hello {username}")
#     print (f"your bill of ${amount} is due: {due_date}")

# display_invoice("mohit",25,"01/01")


# import time

# def count(end,start=0):
#     for x in range (start,end+1):
#         print(x)
#         time.sleep(1)
#     print("done!!")

# count(25,15)

# to generate a phone number

# def get_number(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"

# phone_number = get_number(country=91,area=43,first=99,last=76)

# print(phone_number)

# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg,end=".")
#     for value in kwargs.values():
#         print(value,end=" ")


# shipping_label("Monkey","D","Luffy",
#                street="lane 1",
#                city="emmys lobby",
#                area="east blue sea")

# word game

# word = "choot"
# letter = input("guess a letter in secert word: ")

# if letter in word:
#     print(f"{letter} is there")
# else:
#     print(f"{letter} is not there")

# students = {"sandy","mj","tom"}

# student = input("enter the student name: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} not found")

# def weekend(day):
#     match day:
#         case "sunday" |"saturday":
#                 return True
#         case "monday" | "tuesday"|"wednesday"|"thursday"|"friday":
#                     return False
#         case _:
#                     return "not valid"

# print(weekend("monday"))
    

# python banking program


# import numpy
# import os

# class Balance:
#     def __init__(self):
#         self.amount = 0.0

#     def show_balance(self):
#         print(f"your balance is ${self.amount:.2f}")

#     def deposit(self):
#         amount = float(input("enter the amount you want to deposit: "))

#         if amount <= 0:
#             print("the amount is invalid")
#             return self.amount

#         self.amount += amount
#         print(f"deposit successful: ${amount:.2f}")
#         return self.amount

#     def withdraw(self, accntno, password):
#         amount = float(input("enter the amount you want to withdraw: "))
        
#         if amount <= 0:
#             print("the amount is invalid")
#             return self.amount

#         if amount > self.amount:
#             print("insufficient balance!!")
#             if self.amount <= 0:
#                 print("your balance is too low!!")
#             return self.amount

#         self.amount -= amount
#         print(f"withdrawal successful: ${amount:.2f}")
#         return self.amount


# account = Balance()
# is_running = True
# a = input("acc no.")
# p = input("password.")
# account.withdraw(passw)


# while is_running:
#     print("1. show Balance")
#     print("2. deposit")
#     print("3. withdraw")
#     print("4. Exit")

#     choice = input("enter your choice: ")

#     if choice == '1':
#         account.show_balance()
#     elif choice == '2':
#         account.deposit()
#     elif choice == '3':
#         account.withdraw()
#     elif choice == '4':
#         is_running = False
#     else:
#         print("invalid choice")

# import random 
# import string 


# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# # ENCRIPT
# plain_text =input("enter a message to encript: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"the original message : {plain_text}")
# print(f"encripted message: {cipher_text}")

# # DENCRIPT
# cipher_text =input("enter a message to encript: ")
# plain_text = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]
# print(f"encripted message: {cipher_text}")
# print(f"the original message : {plain_text}")

# hangman in python

import random

words = ("apple", "orange", "banana", "coconut", "pineapple")
# doctionary of keys:()
hangman_art = {0:("   ",
                  "   ",
                  "   "), 
               1:(" o ",
                  "   ",
                  "   "), 
               2:(" o ", 
                  " | ", 
                  "   "), 
               3:(" o ", 
                  "/| ", 
                  "   "), 
               4:(" o  ", 
                  "/|\\", 
                  "    "), 
               5:(" o  ", 
                  "/|\\", 
                  "/  "), 
               6:(" o  ", 
                  "/|\\", 
                  "/ \\")}

def display_man(wrong_guesses):
   for line in hangman_art[wrong_guesses]:
       print(line)
    

def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

# bhosande mc
def main():
    answer = random.choice(words)
    hint = ["_"]* len(answer)
    wrong_guesses = 5
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        display_answer(answer)
        guess = input("enter the letter: ").lower()


if __name__ == "__main__":
    main()
    


    



