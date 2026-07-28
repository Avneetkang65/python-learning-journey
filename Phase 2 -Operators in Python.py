#Arthmetic operator
#Addition operator
a = 1
b = 3
print(a+b)

x = 1.5
y = 2.5
print(x+y)

a1 = "Hell"
b1 = "Avneet"
print(a1 + " "+ b1)

x1 = 2+3j
y1 = 1+5j
print(x1+y1)

w1 = -6
w2 = 3
print(w1+w2)

#Subtraction operator

num1 = 8
num2 = 4
print(num1-num2)

a4 = 5.67
b4 = 2.34
print(a4-b4)

a1 = 5+3j
b2 = 3+8j
print(a1-b2)

#Multiplication operator

n = 3
b = 5
print(n*b)

n1 = 3.5
b1 = 5.5
print(n1*b1)

str = "hello"
print(str*3)

a1 = 2+3j
b1 = 3+5j
print(a1*b1)

#Division operator

a = 15
b = 3
print(a/b)

a1 = 165156.5454
b2 = 65.55
print(a1/b2)

c1 = 3+5j
b2 = 4+5j
print(c1/b2)

#Modulous operator

print(12%3)

a1 = 45.65654
b1 = 4.44449
print(a1%b1)

#Exponent

a = 3
b = 2
print(a**b)

a1 = 655
b1 = 14
print(a1**b1)

a2 = 655.444
b2 = 14.3
print(a2**b2)

#Boolean Operator
a = True
print(type(a))

b = False
print(type(b))

#Comparison Operator
#In python, comparison operators are used to campare values. These operators return Ture or False base on wheather the compaison is ture or false

#Equal to ==
x = 5
y = 10
print(x==y)

x = 5
y = 5
print(x==y)

#Not equal !=

x = 3
y = 2
print(x!=2)

x = 10
y = 10
print(x!=2)

#Greater than >

x = 5
y = 3
print(x>y)

x = 5
y = 13
print(x>y)

#Less than <

x = 5
y = 3
print(x<y)

x = 5
y = 13
print(x<y)

#Greate than or equal to >=

x = 15
y = 5
print(x>=y)

x = 5
y = 15
print(x>=y)

#Less than or equal to <=

x = 5
y = 15
print(x<=y)

x = 15
y = 5
print(x<=y)

#Logical operator

x = True
x = False
print(x and y)

x = True
y = False
print(x or y)

x = True
print(not x)

x = False
print(not x)

#Practice Question

# Question 1 - You have a data containing two record: "Quantity" and "Price per Unit". How would you use arithmetic operators to calculate the total cost for each item, also calculate the total cost? product 1, Quantity -5 , Price per Unit - Rs 250 product 2, Quantity - 25 , Price per Ut - Rs 656 product 3 ,Quantity - 34, Price per Unit - Rs 274

Product_1 = 5*250
Product_2 = 25*656
Product_3 = 34*274
print("The price of product 1 is", Product_1)
print("The price of product 2 is", Product_2)
print("The price of product 2 is", Product_3)
print("The total price customer needs to pay",Product_1+Product_2+Product_3)

# Question 2 - In a finance-based organization, the task is to calculate the simple interest given the principal amount, interest rate, and time period. The interest rate is 8%, the principal amount is Rs 15,00,000, and the time period is 3 years. Calculate the simple interest. Also, the threshold amount is Rs 1,20,000. Please check if the calculated interest is greater or less than the threshold amount.

Principal_amount = 1500000
Interest_rate = 8
Period_of_time = 3

Simple_interest = (Principal_amount * Interest_rate * Period_of_time)/100
Threshold = 120000
print("The Simple Interest is",Simple_interest)
print("The value of simple interest is greater threhold is",Simple_interest>Threshold)

# Question 3 - Write a Python program to calculate the area of a circle with a radius of 12 cm.

pi = 3.14
r = 12
Area_of_circle = (pi * (12**2))
print("The area of circle is",Area_of_circle)
