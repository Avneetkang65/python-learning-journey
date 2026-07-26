#Control flow statment

#If statment

i = int(input("enter your number"))
if i>10:
    print("i is greater than 10")
else:
    print("i is less than 10")

#Question - Develop a temperature converter in Python for a cold storage that converttemperatures between Celsius and Fahrenheit scales. The program should take a temperature value and a unit (C or F) as input. If the temperature is less than 15 degrees Celsius, inform the user that the temperature is not convenient. If the temperature is between 24 to 28 degrees Celsius, inform the user that the temperature is convenient.   

current_temp = int(input("enter the tempature"))

if  current_temp < 15:
    print("temperature is not convenient")
elif current_temp >= 24 and current_temp<= 28:
    print("the temperature is convenient")
else:
    print("temperature is out of scope") 

#Question - Write a program to check whether a person is eligible for voting or not

age = int(input("enter your age"))

if age >= 18:
    print("you are eligibal for the vote")
else:
    print("your are not eligibal for the vote")

#You are tasked with developing a Python program to manage employee salaries for a company. Your program should calculate the net salary of each employee based on their base salary, deductions, and bonuses. Additionally, employees who have been with the company for more than 5 years are eligible for an additional loyalty bonus, 8% of salary. Deductions of tax will be 12%

#Write a Python script that prompts the user to input the following information for each employee: Base salary Years of service After calculating the net salary, the program should print a summary for each employee including their base salary, deductions, bonuses, loyalty bonus (if applicable), and net salary.

base_salary = float(input("Please enter your base salary"))
print("the base salary is",base_salary)

service = int(input("How long you been working in the company"))
print("Year of service",service)

if service > 5:
    total_salary = base_salary + (0.08*base_salary) - (0.12*base_salary)
    print("you will get net salary with loyalty bonus", total_salary)
else:
    net_salary = base_salary - (0.12*base_salary)
    print("your net salary is", net_salary)

#Write a Python program that prompts the user to input a city and displays the famous monument of that city.
#Mumbai: Gateway of India
#KoRkata: Victoria Memorial
#Chennai: Marina Beach
#Bangalore: Botanical Garden
#Pune: Shaniwar Wada
#Write a Python script to implement this functionality.

Mumbai= ("famous monument of that city is Gateway of India") 
Kolkata =("famous monument of that city is Victoria Memorial")  
Chennai=("famous monument of that city is Marina Beach")   
Bangalore= ("famous monument of that city is Botanical Garden")
Pune =("famous monument of that city is Shaniwar Wada") 

city = input("enter your city name")
if city == "Mumbai":
    print("famous monument of that city is Gateway of India")
elif city == "Kolkata":
    print("famous monument of that city is Victoria Memorial")
elif city == "Chennai":
    print("famous monument of that city is Marina Beach") 
elif city == "Bangalore":
    print("famous monument of that city is Botanical Garden")
elif city == "Pune":
    print("famous monument of that city is Shaniwar Wada")
else:
    print("the record is not found")
