#Creating a variable
x = 5
print(x)

a = 10
b = 2.5
c = "Avneet"
print(a,b,c)

y = "we are learning python"
print(y)


# Rules for Python variables:

#A variable name must start with a letter or the underscore character
apple = 23
print (apple)

apple_box = 2.3
print(apple_box)

_ = 5
print(_)

_king = 44.5
print(_king)

#A variable name cannot start with a number
1 = 23
print(1)

1 == 23
print(1)

1_apple = 222
print(1_apple)

apple_1 = 444
print(apple_1)

#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
abc123mds = 25
print(abc123mds)

#Variable names are case-sensitive (age, Age and AGE are three different variables)
age = 23
Age = 25
AGE = 28
aGE = 35
print(age)
print(Age)
print(AGE)
print(aGE)

#A variable name cannot be any of the Python keywords.
print = 14
print(print)


#Data type in python
a = 2
b = 1.5
c = "My name is Avneet"
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

v = 2+3j
print(v)
print(type(v))


num =[22,25,26.5,27]
print(num)
print(type(num))

num1 = True
print(type(num1))

num1 = False
print(type(num1))

#Practice Question
#Question 1
#Imagine you're working on a customer management system, and you have the first name and last name of a customer stored as separate variables. You're developing a customer management system for a retail store. In your database, you have the first name and last name of a customer stored as separate variables: first_name = "John" and last_name = "Doe". How would you concatenate these strings to form the full name "John Doe" for the customer's profile

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

#Question 2
#You have a variable x with the value 5. How would you reassign x to have the value 10?

x = 5
x = 10
print(x)