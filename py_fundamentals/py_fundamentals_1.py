a = 1
b = 10
result = a == b
print(result)  # Output: True

x = 10
print(x)  # Output: 10

x += 5
print(x)  # Output: 15

x -= 5
print(x)  # Output: 10

x /= 5
print(x)  # Output: 2.0

x *= 5
print(x)  # Output: 10.0

#Operator Precedence

'''
()
**
*, /, %
+, -
==, !=, >, <, >=, <=
not
and
or
'''

y = 10 + (5 * 2)
print(y)  # Output: 20


# Type conversion (it can be only done between compatible types)
#int -> float
num_int = 5
num_float = float(num_int)
print(num_float)  # Output: 5.0

#float -> int
num_float = 5.7
num_int = int(num_float)
print(num_int)  # Output: 5

#int -> str
num_int = 10
num_str = str(num_int)
print(num_str)  # Output: '10'

# taking input from user and converting to int

input_a = float(input("Enter a number: "))
input_b = float(input("Enter another number: "))
sum_result = int(input_a + input_b)
print("The sum is:", sum_result)

# average of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print("The average is:", average)
print(result)