#String in python

#crating strings in python

a = "Hello"
print(a)
print(type(a))

b = "I am avneet singh kang \n I am 30 year old"
print(b)
print(type(b))

c = """Hello world
Avneet is another world"""
print(c)

#Indexing of strings

a = "hello dear learners"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

a = "Avneet singh kang"
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])

b = "data science is growing field"
print(b[-1], b[-2], b[-3])

#Slicing

a = "I am learning python"
print(a[0:4])

#Slicing with jump

a = "I am learning python"
print(a[0:10:2])

#Negative slicing

a = "I am learning python"
print(a[-6:-3])

#Question - Write a Python function that takes a date string in the format "YYYY-MM-DD" and returns a tuple containing the year, month, and day as integers.

#Example Input: "2024-05-28"
#Expected Output: (2024, 5, 28)

def extract_date_parts(date_string):
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    day = int(date_string[8:])
    return (year,month,day)

extract_date_parts("2024-05-28")


#write a python program to reverse the string " honesty is the best policy"

str = "honesty is the best policy"
print(str[::-1])

# Lenth method

a = "Avneet"
print(len(a))

a = "Avneet Singh Kang"
print(len(a))

#Strings with spcial symbol

a = "Hello\nworld"
print(a)
print(len(a))

a = """Hello world"""
print(a)
print(len(a))

#Python - Modify the strings

#upper method
#Its help to make captial letter all strings

s = "Hello world"
print(s.upper())

s = "HeLlO wOrLd"
print(s.upper())

#Lower method
#Its help to convert the strings in lower-case

a = "THIS IS MY PYTHON CLASS"
print(a.lower())

#String concatenation

a = "Hello"
b = "world"
print(a + " " + b)

#Replace method - Its help to replace the word

text = "Hello world, I am learning python"
rep = text.replace("python", "data science")
print(rep)

#Index method - Its help to find the word position 

a = "I want to learn"
print(a.index("to"))

#Find method
a = "python is great"
b = a.find("g")
print(b)

a = "I want to learn"
b = a.find("to")
print(b)

#Practice Question 

#Write a Python program that accomplishes the following tasks:

#1) Concatenate the strings "hello" and "world".

a = "Hello"
b = "world"
c = a + " " + b
print(c)


#2) Find the length of the resulting string from the concatenation.

print(len(c))

#3) Extract the substring "world" from the concatenated string.

d = c[5:]
print(d)

#4) Reverse the substring obtained in the previous step

e= d[::-1]
print(e)


#5) Convert the reversed substring to uppercase.
f = e.upper()
print(f)

#6) Replace the letter 'L' with 'X' in the reversed and uppercase substring.

g = f.replace("L", "X")
print(g)