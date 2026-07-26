#Practice Question

# Question 1 - You are developing a program for a math competition where participants need to solve mathematical expressions and provide the result. You want to use Python to automate the evaluation process. Here's how you could approach it:

#1) Take input from the participant to enter a mathematical expression
#2)evaluate the expression entered by the participant and obtain the result.
#)Display the result to the participant.

exprssion = input("enter the mathematical expression")
result = eval(exprssion)
print("The result of the expression is", result)
print("thank you for your participating in the math compition")

#Question 2 - Suppose you're analyzing a dataset containing information about house prices in a city. Each record includes details such as the house size (in square feet), number of bedrooms, and price. You want to perform various calculations and manipulations on this dataset using Python. Answer the following questions: 1) Ask the user 1 & 2 to enter house size, number of rooms they want and .Check the data type user has entered 2)Calculate the price of house , if per sq feet is Rs 5000.3) Threshold price is 75 lakh Rs, which user is paying the price above threshold price.

house_size1 = float(input("enter the sizee of the house"))
house_size2 = float(input("enter the sizee of the house"))
bedroom1 = int(input("enter the bedroon number requirment"))
bedroom2 = int(input("enter the bedroon number requirment"))
print(type(house_size1))
print(type(house_size2))
print(type(bedroom1))
print(type(bedroom2))
cal_house1 = house_size1 * 5000
print("final price for user 1 for the hourse is", cal_house1)
cal_house2 = house_size2 * 5000
print("final price for user 1 for the hourse is",cal_house2)

threhold = 7500000

if cal_house1 > threhold:
    print("user 1 paying above the threhold price")
else:
    print("user 1 is paying below the threhold price")

if cal_house2 > threhold:
    print("user 2 paying above the threhold price")
else:
    print("user 2 is paying below the threhold price")

#Question 3 - You are working on a project to analyze stock market data. Create variables to store the stock symbol, current price, and percentage change in price. Then, calculate the new price after a 10% increase using arithmetic operators. Finally, prompt the user to enter their budget using the input() function, convert it to a float using the float() function, and compare it with the new price

stock_symbol = ("xyz")
current_price = 100
percent_change = 10
new_price = current_price * (1+percent_change/100)
print ("new price of stock is", new_price)

user_bud = int(input("enter your budget"))
a = user_bud >= new_price
print("user budget is greater than new price", a)

#Question - You are working on a project to analyze weather data. Create variables to store the current temperature, the minimum temperature recorded, and the maximum temperature recorded. Determine whether the current temperature is within the range of the minimum and maximum temperatures recorded using logical operators

current_temp = int(input("enter current tempature"))
print(current_temp)
max_temp = int(54)
min_temp = int(24)
print(type(max))
if current_temp >= min_temp and current_price <= max_temp
    print("current tempature within a record to max")
else:
    print("current tempature outside the record")


 #You are given a dataset of student grades and need to determine the grade distribution.
 # Question: Write a Python function grade_distribution(grades) that takes a list of integers representing student grades (0-100). Use a loop to count the number of grades in each grade category:
#'A' (90-100), 'B' (80-89), 'C' (70-79),'D' (60-69), and 'F' (below 60).
#Use if-elif-else statements within the loop to categorize the grades. Return a dictionary with the counts of each grade category.

def grade_distributiion(grades):

    for grade in grades:
        if 90<= grade <=100:
            print("you have got a A grade")
        elif 80<= grade <89:
            print("you got B grade")
        elif 70<= grade >=79:
            print("you got C grade")
        elif 60<= grade >=69:
            print("you got D grade")
        else:
            print("you have got f grade")
    return

grades =[85,65,46,67,99,78,80,88]
grade_distributiion(grades)

#Question - You're creating a number guessing game where the computer generates a random number between 1 and 100, and the player has to guess it. 

#Write Python code to generate a random number between 1 and 100. Use control flow statements and loops to allow the player to guess the number and provide feedback (too high, too low, or correct). Define a user-defined function to encapsulate the game logic and call this function to play the game.

import random

def number_guess():
    secret = random.randint(1,100)
    print(secret)

    print("welcome to the number guessing game")
    print("I have choosen the number between 1 to 100, can you guess it")

    attempts = 0
    guess = None

    while guess != secret:

        guess = int(input("enter your guess number"))
        attempts = attempts+1

        if guess < secret:
            print("too low, please try agian")
        elif guess > secret:
            print("too high, try again")
        else:
            print("your have guess correct answer :) ")
            print("the number of attempts you have used", attempts)

number_guess()

#Question - You're tasked with creating a program to calculate the sum of squares of the first n natural numbers, where n is entered by the user.

#Write Python code to prompt the user to enter a positive integer n. Use a loop to calculate the sum of squares of the first n natural numbers. Define a user-defined function to encapsulate the sum of squares calculation logic and call this function with the user's input.

def square_of_natural(n):
    total = 0

    for i in range(1,n+1):
        total = i**2
              
    return total

n= abs(int(input("enter your number")))
square_of_natural(n)

answer = square_of_natural(n)
print(answer)
