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

n = 0
while (n <= 10):
    if (n % 3 == 0):
        n+=1
        continue
    print(n)
    n+=1
    
print("JOB DONE")