# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruit_list = ["apple" , "pear" , "orange " , "pineaple"]
# TODO: Use a for loop to print each fruit in the list
for fruit in fruit_list:
    print(fruit)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count-= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
square_numbers= [ 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
for number in square_numbers:
    print(number)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colour_list = [ "blue ", "white ", "navy ", "red ", "yellow ", "black " , "purple " ,"pink " ]
# TODO: Use a for loop to select and print 3 random colors from the list
for colours in range(3):
    colours = random.choice(colour_list)
    print(colours)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operation

# TODO: Use a while loop to create a simple calculator
def calculator():
    while True:
        # Ask for operation
        operation = input("Enter an operation (+, -, *, /) or 'exit' to quit: ")
        if operation.lower() == 'exit':
            print("Exiting the calculator.")
            break
        # Ask for numbers
        try:
            num1 = float(input("Enter number 1 here: "))
            num2 = float(input("Enter number 2 here: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        # Perform the chosen operation
        if operation == "+":
            result = math_operation.add(num1, num2)
        elif operation == "-":
            result = math_operation.subtract(num1, num2)
        elif operation == "*":
            result = math_operation.multiply(num1, num2)
        elif operation == "/":
            result = math_operation.divide(num1, num2)
            if result == "Error: Division by zero":
                print(result)
                continue
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
            continue
        # Print the result
        print(f"The result is: {result}")
calculator()