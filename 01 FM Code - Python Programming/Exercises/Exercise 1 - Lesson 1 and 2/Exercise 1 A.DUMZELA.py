# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("What is your name?")
# TODO: Ask the user for their age and store it in a variable
age = input("What is your age?")
# TODO: Print a greeting using the name and age variables
print(f"Hello, {name} !You are {age} years old.")
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("write the length of the rectangle: "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("write the width of the rectangle: "))
# TODO: Calculate the area of the rectangle
area = width * length
# TODO: Print the result
print(f"the area of the rectangle: {area}")
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temperature = float(input("write the temperature in celsius: "))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
convert = (temperature *9/5) + 32
# TODO: Print the result rounded to two decimal places
print(round(convert,2))