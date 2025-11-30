# Conditional Statements

# color = input("Enter color : ")

# if color == "red":
#     print("STOP")
# elif color == "green":
#     print("GO")
# elif color == "yellow":
#     print("WAIT")
# else:
#     print("Invalid color value!")
    
# Age

# <13 child
# 13-18
# 18+

# age = int(input("Enter the age of the person: "))

# if age <= 13:
#     print("The person is a child")
# elif age > 13 and age < 18:
#     print("The person is a teenager")
# else:
#     print("The person is an adult")

# multiple of 5 or not

# n = int(input("Enter the value of n : "))

# if(n%5 == 0):
#     print(f" The number you have entered is Multiple of 5")
# else:
#     print("Not a multiple of 5")
    
# # Odd or even

# n = int(input("Enter the value of n : "))

# if(n%2 == 0):
#     print(f"EVEN!!!!")
# else:
#     print("ODD")


# Match Case Statement in python

# Nested conditionals example#
# ----------------------------------------------------------------

# color = input('enter color : ')

# match color:
#     case "Green":
#         print("Green")
#     case "Red":
#         print("Red")
#     case "Blue":
#         print("Blue")
#     case "Narangi":
#         print("Orange")
#     case _:
#         print("Wrong Color")

# Less goo for loops

# count = 0 # iterator
# while count <= 5:
#     print(count)
#     count += 1
    
# i = 1
# n = 5   
# while (i<=10):
#     print(n, " * ", i, " = ", (n*i))
#     i+=1
    
# We use Break statement to end the loop
# & Continue statement to skip the record

# If i dont want any multiple of 3 from a 1-10 & print the remaining numbers we can use it

# n = 0
# while (n <= 10):
#     if (n % 3 == 0):
#         n+=1
#         continue
#     print(n)
#     n+=1
# print("JOB DONE")

# Range function -> it generates sequences

# range(5) means -> 0 to 4
# there is 3 parameters in range function range(start value, stop value, stepup value) the start value & step up values are optional they are by default 0 & +1 respectively so we pass the stop value only

# print all the odd numbers till 50 using range function

# for i in range(0,51,2):
#     print(i)
    

# # print sum of first 'n' natural numbers
# # we want 1 + 2 + 3 + 4 + 5 ,..., + 100 = answer

# n = 100
# sum = 0

# for i in range(0,101,1):
#     sum += i

# print(sum)


# Function

def sum(a,b):
    s = a+b
    print(s)

sum(4,5)
sum(5,5)

# Average calculating function

def cal_average(a,b,c):
    sum = a+b+c
    return sum/3

print(cal_average(10,20,30))
# PYTHON FUNDAMENTALS 2 — LEARNING NOTES WITH CLEAN EXAMPLES

# -------------------------------------------------------------
# CONDITIONAL STATEMENTS
# -------------------------------------------------------------

# Basic if-elif-else example
color = input("Enter a color (red/green/yellow): ")

if color.lower() == "red":
    print("STOP")
elif color.lower() == "green":
    print("GO")
elif color.lower() == "yellow":
    print("WAIT")
else:
    print("Invalid color value!")


# -------------------------------------------------------------
# AGE CLASSIFICATION
# -------------------------------------------------------------

age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")


# -------------------------------------------------------------
# MULTIPLE OF 5 CHECK
# -------------------------------------------------------------

n = int(input("Enter a number: "))
if n % 5 == 0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")


# -------------------------------------------------------------
# ODD / EVEN CHECK
# -------------------------------------------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# -------------------------------------------------------------
# MATCH CASE STATEMENT (Python 3.10+)
# -------------------------------------------------------------

shade = input("Enter any color name: ")

match shade:
    case "Green":
        print("Color is Green")
    case "Red":
        print("Color is Red")
    case "Blue":
        print("Color is Blue")
    case "Narangi":
        print("Color is Orange")
    case _:
        print("Unknown Color")


# -------------------------------------------------------------
# WHILE LOOPS
# -------------------------------------------------------------

# Print numbers 0–5
count = 0
while count <= 5:
    print(count)
    count += 1

# Print multiplication table of a number
table_num = int(input("Enter a number for multiplication table: "))
i = 1

while i <= 10:
    print(table_num, "*", i, "=", table_num * i)
    i += 1


# -------------------------------------------------------------
# BREAK & CONTINUE
# -------------------------------------------------------------

# Print numbers from 1–10 except multiples of 3
x = 1
while x <= 10:
    if x % 3 == 0:
        x += 1
        continue
    print(x)
    x += 1


# -------------------------------------------------------------
# RANGE FUNCTION BASICS
# -------------------------------------------------------------

# range(stop)
# range(start, stop)
# range(start, stop, step)

# Print odd numbers up to 50
for i in range(1, 51, 2):
    print(i)


# -------------------------------------------------------------
# SUM OF FIRST N NATURAL NUMBERS
# -------------------------------------------------------------

N = int(input("Enter N: "))
total = 0

for i in range(1, N+1):
    total += i

print("Sum of first", N, "natural numbers is:", total)


# -------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------

# Example 1: Add two numbers
def add(a, b):
    return a + b

print("Add 4 and 5:", add(4, 5))


# Example 2: Calculate average of three numbers
def calculate_average(a, b, c):
    total = a + b + c
    return total / 3

print("Average of 10, 20, 30:", calculate_average(10, 20, 30))

