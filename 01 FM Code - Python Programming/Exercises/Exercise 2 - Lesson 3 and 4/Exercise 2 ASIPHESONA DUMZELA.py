# Question 1: Arithmetic and Assignment Operators

# # TODO: Add 3 to x using the += operator
# x = 28
# x += 3
# # TODO: Multiply y by 2 using the *= operator
# y = 5
# y *= 2
# # TODO: Divide x by y and store the result in a variable called 'result'
# result = x/y 
# # TODO: Print the value of 'result'
# print(result)
# #------------------------------------------------------------------------------------
# # Question 2: Comparison and Logical Operators

# # TODO: Create a condition that checks if a is greater than b
# a = 31
# b = 10 
# c = 3

# check = a > b 
# # TODO: Create a condition that checks if b is even (hint: use the modulus operator)
# check2 = b % 2 
# # TODO: Create a condition that checks if c is less than or equal to a
# check = c <= a 
# # TODO: Combine the above conditions using logical operators to create a 'final_condition'
# #       The 'final_condition' should be True if either:
# #       - a is greater than b, or
# #       - b is even and c is less than or equal to a
# final_condition = (a>b) or (b % 2) and (c <= a)

# # TODO: Print the value of 'final_condition'
# print(final_condition)
# #------------------------------------------------------------------------------------
# # Question 3: Conditional Statements

# # TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
# score = int(input("Enter your score: " ))
# # TODO: Implement a grading system using if-elif-else statements:
# #       90-100: A
# #       80-89: B
# #       70-79: C
# #       60-69: D
# #       Below 60: F
# if score >=90 and score <=100:
#     grade = "A"
# elif score >=80 and score <=89:
#     grade = "B"
# elif score >=70 and score <=79:
#     grade = "C"
# elif score >=60 and score <=69:
#     grade = "D"
# else:
#     grade = "F"

# # TODO: Print the grade for the given score
# print(grade)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input(" enter number 1: "))
num2 = int(input(" enter number 2: "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation =input("Enter an operation (+, -, *, /)")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+" :
    answer = num1 + num2
elif operation == "-" :
    answer = num1 - num2
elif operation == " * " :
    answer = num1 * num2
elif operation == " / " :
    if num2 != 0 :
        answer = num1 / num2 
    else :
        print("error") 
# TODO: Handle the case of division by zero
    print("error")
# TODO: Print the result of the operation
print(answer) 