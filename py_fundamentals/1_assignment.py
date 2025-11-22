# Q1 WAP that asks the user for their name & age, then prints a sentence like this:
# Hello Shradha, you are 21 years old!

# name = input("Enter your name : ")
# age = input("Enter your age :")

# print("Hello " + name +", you are " + age + " years old!")


# Q2 Take two numbers as input from the user and print their sum, difference, product, and quotient.

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# sum = int(num1 + num2)
# print(f"Sum : ", sum)

# difference = num1 - num2
# print(f"Difference : ", difference)

# product = num1 * num2
# print(f"Product : ", product)

# quotient = num1 / num2
# print(f"Quotient : ", quotient)

# Q3 Ask the user to enter two integers and one float. Convert them all to floats and print their average.

# a = int(input("Enter first number : "))
# b = float(input("Enter second number : "))

# # Converting 'em into floats

# a = float(a)
# print(f"After Converting : ", a)

# average = (a + b)/ 2

# print(f"Average of ", a ," & ", b ," is : ", average)

# Q4 The user enters a string containing a number (e.g.,"45"). Convert it into
# An integer
# A Float
# A String Again
# Print all three values with their types.

# original_string = str(input("Enter the string containing a number : "))
# print(f"Original String : ", original_string)

# converted_int = int(original_string)
# print(f"Value of Original String after converting it into " , type(converted_int), " is : ", converted_int)

# converted_float = float(original_string)
# print(f"Value of Original String after converting it into " , type(converted_float), " is : ", converted_float)

# converted_string = str(original_string)
# print(f"Value of Original String after converting it into " , type(converted_string), " is : ", converted_string)

# Q5 Evaluate and print the result of the following expression:
# x = 10 + 3 * 2 ** 2
# Explain why the output is what it is.

# According to operator precedence:
# 1. ** (exponent) runs first → 2 ** 2 = 4
# 2. * runs next → 3 * 4 = 12
# 3. + runs last → 10 + 12 = 22

# So the final result is 22.

# Q6 WAP to swap values of two numbers entered by the user.

# value1 = int(input("Enter value one: "))
# value2 = int(input("Enter value two: "))

# print("Before Swapping Value 1:", value1)
# print("Before Swapping Value 2:", value2)

# temp = value2
# value2 = value1
# value1 = temp

# print("After Swapping Value 1:", value1)
# print("After Swapping Value 2:", value2)

# Q7 Ask the user for a temperature in Celsius (string input). Convert it into float, then calculate the temperature in Fahrenheit.

# temperatureInCelcius = str(input("Enter the value of temperature in Celcius : "))
# convertedValueOfCelcius = float(temperatureInCelcius)
# print(f"Converted Value Of Celcius : ",convertedValueOfCelcius)
# temperatureInFahrenheit = (convertedValueOfCelcius * (9/5)) + 32

# print(f"Value of Temperature in Fahrenheit is : ", temperatureInFahrenheit)

# Q8 Take the radius (r) as user input and print the area.
# Formula: Area = pi * r^2  (pi = 3.14)

# radius = float(input("Enter Radius: "))
# pi = 3.14
# area = pi * radius * radius

# print("Area is:", area)

# Q9 Ask the user for Principal (P), Rate (R), Time (T). 
# Convert all to float and compute Simple Interest.
# Formula: SI = (P * R * T) / 100

# p = float(input("Enter Principal: "))
# r = float(input("Enter Rate: "))
# t = float(input("Enter Time: "))

# si = (p * r * t) / 100

# print("Simple Interest is:", si)

# Q10 Take a decimal number as input (like 45.78) and output its:
# integer part -> 45
# fractional part -> .78

number = float(input("Enter the number like 45.78 : "))
integerPart = int(number)
print(f"The integer part is this : ",integerPart)

fractionalPart = number - integerPart 
print("The fractional part is: ", f"{fractionalPart:.2f}"[1:])