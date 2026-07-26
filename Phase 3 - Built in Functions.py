#Built Functions

#Float functions

num_int = 10
print(num_int)
print(type(num_int))
a = float(num_int)
print(a)
print(type(a))

a = "3.14"
print(a)
print(type(a))
b = float(a)
print(b)
print(type(b))

#Int Function

a = 5.59649
print(a)
print(type(a))
c = int(a)
print(c)
print(type(c))

a1 = "22"
print(a1)
print(type(a1))
b1 = int(a1)
print(b1)
print(type(b1))

# Str function

a = 56
print(a)
print(type(a))
b = str(a)
print(b)
print(type(b))
c = "2"
print(b+c) # It is show the result 562 because addition not apply in string

x = 5.554546654
print(x)
print(type(x))
y = str(x)
print(y)
print(type(y))

#Complex function

comp = complex(2,3)
print(comp)


#Abs Function

x = -54.544
print(abs(x))

y = -541654
print(abs(y))

z = -3+4j
print(abs(z))

#Length function

a = "Hello, I am avneet kang"
print(a)
print(len(a))

c = [52,5,55,78,5484,61]
print(c)
print(len(c))

# Practie Questons

#Question 1 - In a game application, the player's score is stored as a floating-point number. However, for leaderboard display, you need to convert the score to an integer. How would you use the int() function to convert the player's score from floating-point to integer format? pls solve this with code, player score = 1234.56

Score = 1234.56
print(int(Score))

score_int = int(Score)
print(score_int)

#Question 2 - In a customer relationship management (CRM) system for a retail company, you have a database containing customer records. How would you use the len() function to find the total number of customers in the database, allowing the company to track its customer base?
customer_database = [
(1, 'John Doe', 'john@example.com'),
(2, 'Jane Smith', 'jane@example.com'),
(3, 'Alice Johnson', 'alice@example.com'),]

customer_database = [
(1, 'John Doe', 'john@example.com'),
(2, 'Jane Smith', 'jane@example.com'),
(3, 'Alice Johnson', 'alice@example.com'),]
print("the total number of customer in the database is", len(customer_database))

#Question 3 - You're developing a financial application that calculates simple interest. The principal amount is 250000 Rs, the interest rate is 9.34567%, and the time period is 3 vears. Calculate the Simple Interest (SI), and the final value should bran integer.

p = 250000
i = 9.34567
t = 3

si = int((p*i*t)/100)
print(si)

#Bin Function

binary_rep =  bin(10)
print(binary_rep)

#sum function

#The sum() function in Python is used to calculate the sum of elements in an iterable, such as lists, tuples, and other iterable objects.

mylist = [61,21321,21,564,21,21,54,]
a = sum(mylist)
print(a)
print(type(a))

a = [1,2,3,4,5]
starting_value = 10
total = sum(a,starting_value)
print(total) 

#Eval function

x = 10
y = 5
experession = "x+y*2"
print(eval(experession))


#Help function

#The Python help function is used to display the documentation of modules, functions, classes, keywords, etc

help(print)

help(sum)

#input function

name = input("Please enter your name")
print("my name is ", name)
print(type(name))

#Practice Question

#Question 1

#Get two number from the user and calculate their sum

num1 = int(input("enter first number"))
num2 = int(input("enter your second number"))
sum=(num1+num2)
print(sum)
print(type(sum))

#Question 2

#As part of your role in a data-driven project, you need to take input from the user for their age, weight, and height. However, there's an issue: the user has entered their age as a negative number. You need to correct the age of the user, and after correcting the age, calculate their Basal Metabolic R using the Harris-Benedict equation for men.

#Ensure that the final answer of BMR is an integer. Basal Metabolic Rate (BMR): Formula (Harris-Benedict equation for men): BMR = 88.362 + (13.397 * weight in kg) +(4.799 * height in cm) - (5.677 * age in years)

age =int(input("enter your age"))
weight = int(input("enter your weight"))
height = float(input("enter your heght"))
correct_age = abs(age)

BMR = "88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * correct_age)"
bmr = eval(BMR)
print(int(bmr))

#Question 3
#write a python code for hostel students, ask them to mention thier course name and age. for 5 students and calculate thier avg age.

stuent1 = int(input("Please enter your age student 1 - "))
course1 = input("Enter your course name: ")
stuent2 = int(input("Please enter your age student 2 - "))
course2 = input("Enter your course name: ")
stuent3 = int(input("Please enter your age student 3 - "))
course3 = input("Enter your course name: ")
stuent4 = int(input("Please enter your age student 4 - "))
course4 = input("Enter your course name: ")
stuent5 = int(input("Please enter your age student 5 - "))
course5 = input("Enter your course name: ")
cal_age = "(stuent1+stuent2+stuent3+stuent4+stuent5)/5"
avg_age =eval(cal_age)
print(avg_age)