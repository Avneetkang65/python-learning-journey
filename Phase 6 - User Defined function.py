#User Defined function
#A user-defined function in Python is a function created by the programmer to perform a specific task or set of tasks. Unlike built-in functions in Python, wnich are predefined and provided by the Python language itself, user-defined functions are defined by the programmer based on their requirements These functions allow you to encapsulate a block of code that can be called and executed multiple times throughout your program, improving code organization, readabilty- reusability.

#creating and calling a funcation
def avneet(): #Here we are creating the def function
    print("Hello, this is avneet")

avneet() #Here we calling the function

def details_bill():
    print("the last date of the bill payment is on next week sunday")
    print("after the deadline, you need to pay Rs 1000 as a fine")
    print("pay your bill soon")

for i in range(3):
    cust_nam = input("enter your name")
    elec_cuns = int(input("enter the unit which has been consumed"))
    bill = elec_cuns*10
    print("total amount of bill you need to pay",bill)
    details_bill()

#Agruments

#create a function, which checks the number is even or odd

def check_even_odd(number):
    if number%2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

check_even_odd(5)

# 2 Agruments

def my_name(fname, lname):
    print(fname + " " + lname)

my_name("Avneet","singh")

#Write a user-defined function to process the exam scores and calculate the following statistics:
# The average exam score.
# The highest exam score.
# The lowest exam score.
# The number of students who passed the exam (assuming a passing score is 80 or above).
# The number of students who failed the exam.
# 
# exam_scores = [85, 92, 78, 90, 88, 95, 82, 79, 87, 91]

def cal_exam_stat(exam_score):

    num_student = len(exam_score)
    average_score = sum(exam_score)/num_student
    highest_exam = max(exam_score)
    lowest_exam = min(exam_score)

    num_passed = 0

    for score in exam_score:
        if score>=80:
            num_passed = num_passed+1
        
    num_failed = num_student-num_passed

    return average_score, highest_exam,lowest_exam,num_passed,num_failed

exam_score = [85, 92, 78, 90, 88, 95, 82, 79, 87, 91]

average_score, highest_exam,lowest_exam,num_passed,num_failed = cal_exam_stat(exam_score)

print("the average socre is", average_score)
print("the highest score is", highest_exam)
print("lowest score is", lowest_exam)
print("the number of student passed", num_passed)
print("the number of student failed", num_failed)