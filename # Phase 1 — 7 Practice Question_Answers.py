# Phase 1 — Variables & Data Types

#Question 1 - Create three variables to store a product's name, price, and in_stock status (True/False). Print each variable along with its data type using type().

product_name = "Mobile"
product_price = 36000
in_stock = True
print(product_name)
print(type(product_name))
print(product_price)
print(type(product_price))
print(in_stock)
print(type(in_stock))

#Question 2 - user enters their weight in a text field, so it comes in as a string, e.g. "68.5". Convert it to a float, then print the value and confirm its new type.

weight = input("enter your weight")
print("your weight is", weight)
print(type(weight))
int_weight = int(weight)
print(int_weight)
print(type(int_weight))

#Question 3 - You're given celsius = 100. Without changing the original variable, create a new variable fahrenheit using the formula (celsius * 9/5) + 32 and print the result.

celsius = 100
fahrenheit = (celsius * 9/5) + 32 
print("fahrehnit", fahrenheit)
print("celsius", celsius)

#Phase 2 — Operators

#Question 4 - A cinema charges $12 per ticket. Write code that calculates the total cost for 4 tickets, then applies a 15% discount if the customer has a loyalty card (has_loyalty_card = True). Print the final price.

ticket = 12
num_ticket = 4
has_loyalty_card = True

total_cost = ticket*num_ticket
if has_loyalty_card:
    total_cost = total_cost -(total_cost-0.15)

print("Final price is", total_cost)

#Question 5 - Given a = 17 and b = 5, print the result of integer division (//) and the remainder (%) in the same print statement, clearly labeled.

a = 17
b = 7
print("17 // 5 =", a//b,"and 17 % 5 =", a%b)

#Question 6 - Write code that checks two conditions using logical operators: a user can enter a competition only if age >= 18 and country == "India". Test it with sample values and print whether they're eligible.

age = int(input("enter your age"))
country = input("Please enter your country")
eligible = age>18 and country == "India"
print("Eligible for the competion", eligible)

#Phase 3 — Built-in Functions

#Question 7 - You have prices = [199.99, 45.50, 999.00, 12.25]. Use built-in functions to print: the number of items, the sum of all prices, the most expensive price, and the cheapest price.

princes = [199.99, 45.50, 999.00, 12.25]
num_item = len(princes)
sum_price = sum(princes)
max_price = max(princes)
min_price = min(princes)
print("the number of items are" ,num_item)
print("sum of price is ",sum_price)
print("the most expersive price is ",max_price)
print("the cheapest price is ", min_price)

#Question 8 - A user enters their favorite number as text. Convert it to an integer and use abs() to make sure it's printed as a positive number even if they entered something negative.

number = int(input("Please enter your favorite number"))
print("Favorute number is", abs(number))

#Question 9 - Given sentence = "Python is fun to learn", use len() to print how many characters it contains, and use str()/int() conversions to combine that length with the number 100 (e.g. print "Total: " + str(length + 100)).

sentence = "Python is fun to learn"
leth_sentence = len(sentence)
print(leth_sentence)
print("Total: " + str(leth_sentence + 100))

#Phase 4 — Control Flow

#Queston 10 - Write a simple ATM PIN checker. Store a correct_pin = "4521". Ask the user to input a PIN and print "Access granted" if it matches, or "Access denied" otherwise.

pin = abs(int(input("Please enter your ATM PIN")))
correct_pin = int(4521)
if correct_pin == pin:
    print("Access granted")
else:
    print("Acess denied")

#Questiom 11 - Write a program that takes a person's age as input and prints their life stage: "Child" (0–12), "Teenager" (13–19), "Adult" (20–59), or "Senior" (60+).

age = abs(int(input("Please enter your age")))
if age <= 12:
    print("Child")
elif age <=19:
    print("Teenager")
elif age <=59:
    print("Adult")
else:
    print("Senior")

#Question 12 - A shipping company charges based on package weight: under 1kg is free, 1–5kg costs $5, 5–10kg costs $10, and anything above 10kg costs $20. Take the weight as input and print the shipping cost.

package_weight = abs(float(input("Please enter the weight of your product")))
if package_weight <1:
    print("Packge cost is free")
elif package_weight <=5:
    print("The price of package is", package_weight*5)
elif package_weight <=10:
        print("The price of package is", package_weight*10)
else:
    print("The price of package is", package_weight*20)

# Phase 5 — Loops

#Question 13 - Print all numbers from 1 to 30 that are divisible by 3 or 5, using a for loop and range(). 

for  i in range (1,31):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

#Question 14 - Write a program using a while loop that keeps asking the user to enter a password until they type "exit", then prints "Goodbye!".

while True:
    password = input("Enter your password (or 'exit' to quit)")
    if password == "exit":
        print("Good Bye")
        break


#Question 15 - Given numbers = [4, 12, 7, 19, 3, 25, 8], use a for loop to find and print the largest number without using the built-in max() function.

numbers = [4, 12, 7, 19, 3, 25, 8]
large_num = 0

for i in numbers:
    if i>large_num:
        large_num = i
print("Largest number is", large_num)

#Question 16 -  Write a program that prints a countdown from 10 to 1, then prints "Liftoff!". Use break if the countdown reaches a number the user specifies as a "skip point" (bonus challenge).

skip_point = abs(int(input("Please enter your skip point")))

for count in range (10,0,-1):
    if count == skip_point:
        break
    print(count)
print("Liftoff!")

#Phase 6 — User-Defined Functions

#Question 17 - Write a function is_prime(number) that returns True if the number is prime and False otherwise. Test it on a few values.   

def is_prime(number):
    if number <=1:
        return False
    
    for i in range (2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(5))

#Question 18 - Write a function calculate_bmi(weight_kg, height_m) that returns the BMI using the formula weight / (height ** 2), rounded to 1 decimal place.

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 1)
    
  
weight = float(input("enter your weight"))
height = float(input("enter your height"))
print(calculate_bmi(weight, height))

#Question 19 - Write a function word_count(sentence) that takes a sentence and returns the number of words in it (hint: look up the .split() string method).

def word_count(sentence):
    lenth_sen = (len(sentence.split()))
    return lenth_sen

sentence = input("please enter your sentence")
print(word_count(sentence))

#Phase 7 — Strings

#Question 20 - Given email = "avneet.kang@example.com", extract and print just the username part (avneet.kang) using string slicing or the .split() method.

email = "avneet.kang@example.com"
user_name = email.split("@")[0]

print(user_name)

#Question 21 - Write a function is_palindrome(word) that returns True if a word reads the same forwards and backwards (e.g. "madam"), and False otherwise.

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input("enter your word")
print(is_palindrome(word))

#Question 22 - Given full_name = " avneet SINGH kang ", clean it up so it prints as "Avneet Singh Kang" — properly capitalized with no extra spaces at the start/end. (Hint: look up .strip() and .title().)

full_name = " avneet SINGH kang "

clean_name = (full_name.strip())

print(clean_name.title())
