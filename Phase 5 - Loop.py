#Loop

#While loop

count = 1
while count <=5:
    print(count)
    count = count+1

#Write a Python program to print all the even numbers between 1 and 50 using a while loop

num = 1
while num <=50:
    if num%2 ==0:
        print(num)
    num = num+1

#While loop , using if else
#You are tasked with validating user input for email addresses. Write a Python program that prompts the user to enter an email address. Use a while loop to iterate through the input and check if the email address contains an "@" symbol and a "." symbol. If the email address does not meet these criteria, print "Invalid email address format. Please try again." Otherwise, print "Email address validation passed

email = input("Enter your email address")
print(email)

valid_email = False

while not valid_email:
    if "@" in email and "." in email:
        print("Email adress validation passed")
        valid_email = True
    else:
        print("Invaild email address format, please try again")
        email = input("Please enter your email address")

#For loop in python

num = [1,2,3,4,5]
for i in num:
    print(i)


nam = "Students"
for i in nam:
    print(i)

#range
for i in range(11):
    print(i)


for i in range(4,11): #it will start from 4 to till 10
    print(i)


#for loop and if condition

for i in range(26):
    if i %2 == 0:
        print("the number is even",i)

for i in range(26):
    if i %2 == 0:
        print("the number is even",i)
    else:
        print("the number is odd",i)

#Implement a Python program to generate the multiplication table of a given number using a for loop.

num = int(input("enter your number for multiplcation"))
print("The mulitplication table of", num)

for i in range (11):
    print(f"{num} X {i} = {num*i}")

#Practice Question

#You are tasked with creating a program to assist shoppers in calculating their total bill at a grocery store. The store offers discounts based on the total purchase amount. Your task is to implement a Python program that takes the price of each item purchased and calculates the total bill, including any applicable discounts.

#The store offers the following discount rates based on the total purchase amount:

#If the total purchase amount is $100 or more, the customer receives a 10% discount.

#If the total purchase amount is between $50 and $99.99, the customer receives a 5% discount.

#Write a Python program to prompt the user to enter the prices of the items they purchased. Use a for loop to iterate through the prices entered and calculate the subtotal. Apply the appropriate discount based on the total purchase amount using if-else statements. Finally, print out the subtotal, discount amount (if any), and the total bill after applying the discount.

num_items = int(input("enter the number of items purschased"))
total_price = 0

for i in range(num_items):
    price = float(input("enter the price of items"))
    total_price = total_price+price
    i+1
if total_price >= 100:
    discount = 0.10 * total_price
elif 50<= total_price <100:
    discount = 0.5 * total_price
else: 
    discount = 0

total_bill = total_price - discount
print("subtotal", total_bill)

#Break statment
#we can use the break statement with the loop to termiate the loop when a certain condition is met.

for i in range(10):
    if i == 4:
        break
    print(i)

#Continue statement
#The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.

for i in range(10):
    if i == 4:
        continue
    print(i)
print("I am learning")