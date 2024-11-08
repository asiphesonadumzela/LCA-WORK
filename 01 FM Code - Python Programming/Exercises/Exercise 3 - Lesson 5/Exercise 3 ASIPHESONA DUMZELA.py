# Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"
def greet(name):
    print("hello "+ name )
# TODO: Call the 'greet' function
greet("world")

#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalized_greeting(name):
    print("hey "+ name)
# TODO: Call the 'personalized_greeting' function with your name
personalized_greeting("Asiphesona")

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number as a parameter and returns its square
def square(number) :
    answer= number*number
    print(answer)
    return answer
# TODO: Call the 'square' function with the number 5 and print the result
square(5)

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length,width) :
    rectangle_area=length*width
    print(rectangle_area)
    return rectangle_area
# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result
rectangle_area(4,5)

#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(function,number) :
    return function(number)
# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double(number):
    return number + number
# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
print(apply_operation(double,7))
# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
print(apply_operation(square,3))