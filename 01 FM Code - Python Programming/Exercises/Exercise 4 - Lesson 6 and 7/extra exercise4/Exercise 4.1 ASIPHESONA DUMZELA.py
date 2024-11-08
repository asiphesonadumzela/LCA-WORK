#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.
def check_attendance(students,absentees):
    absente_students = []
    present_students = []

    for student in students:
        if student in absentees:
            absente_students.append(student)
        else:
            present_students.append(student) 

    return absente_students,present_students

# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.
students = ["Alice", "Bob", "Charlie", "David"]
absentees = ["Bob", "David"]
present, absent = check_attendance(students, absentees)

print("Present students:", present)
print("Absent students:", absent)
#------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.
def calculate_average_grade(students):
    total = sum(students.values())
    count = len(students)
    average = total / count 
    return average

students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

# Calculate and print the average grade
average_grade = calculate_average_grade(students)
print("The average grade of the class is:", average_grade)
#------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.

def operation_selector(operation):
    # Define the inner functions for adding and multiplying
    def add(x, y):
        return x + y
    
    def multiply(x, y):
        return x * y
    
    if operation == "add":
        return add
    elif operation == "multiply":
        return multiply
    else:
        return None  # Handle invalid operation

# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
add_function = operation_selector("add")
result_add = add_function(4, 6)
print(result_add)  # Output: 10

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.
multiply_function = operation_selector("multiply")
result_multiply = multiply_function(3, 7)
print(result_multiply)
#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)
distance = 150  
fuel_efficiency = 15  
fuel_price = 1.5  
def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    
    
    fuel_needed = distance / fuel_efficiency
    
    total_cost = fuel_needed * fuel_price
    
    return total_cost


cost = calculate_trip_cost(distance, fuel_efficiency, fuel_price)
print(f"The total cost of the trip is: ${round(cost,2)}")

# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}

# TODO: Use a for loop to print each item and its quantity in stock.
for item,quantity in grocery_inventory.items():
    print(f"{item}: {quantity}")
# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).
total= sum(grocery_inventory.values())
print(total)
    

# #------------------------------------------------------------------------------------
# # Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# # TODO: Ask the user to input their PIN.
# # TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.        
# # TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".

# correct_pin = "1234"
# attempts = 0

# # TODO: Use a while loop to implement the retry system.

pin = "123456"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    guessed_pin = input("Enter your pin: ")
    
    if guessed_pin == pin:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Incorrect pin. Please try again.")
        if attempts == max_attempts:
            print("You have reached the maximum number of incorrect attempts.")
            print("Account Locked")
            retry = input("Do you want to try again? (yes/no): ")
            if     retry.lower() == "yes":
                attempts = 0  
            else:
                print("Have a good day!")
        

# #------------------------------------------------------------------------------------
import random

# List of 10 random assignment scores between 0 and 100.
scores = [random.randint(0, 100) for _ in range(10)]

# Calculate the total score using a for loop.
total_score = 0
for score in scores:
    total_score += score

# Calculate the average score.
average_score = total_score / len(scores)

# Print total and average scores.
print(f"Scores: {scores}")
print(f"Total Score: {total_score}")
print(f"Average Score: {round(average_score,2)}")

# Bonus: Print congratulatory message if average is above 75.
if average_score > 75:
    print("Congratulations! The class performed well with an average score above 75.")
else:
    print("Keep pushing! There's room for improvement.")
# #------------------------------------------------------------------------------------
import random

# List of 20 participants.
participants = ["Person1", "Person2", "Person3", "Person4", "Person5", "Person6", "Person7", 
                "Person8", "Person9", "Person10", "Person11", "Person12", "Person13", 
                "Person14", "Person15", "Person16", "Person17", "Person18", "Person19", "Person20"]

# Randomly select 5 participants from the list.
selected_team = random.sample(participants, 5)

# Print the selected team members.
print("Selected Team Members:")
for member in selected_team:
    print(member)


# #------------------------------------------------------------------------------------
# # Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# # Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""

# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.
import fitness_tracker
# # TODO: Ask the user to input the distance they walked, ran, and cycled today.
walked_km = float(input("Enter the distance you walked today (in km): "))
ran_km = float(input("Enter the distance you ran today (in km): "))
cycled_km = float(input("Enter the distance you cycled today (in km): "))
# # TODO: Calculate and print the total calories burned for each activity.
calories_walked = fitness_tracker.walk_calories(walked_km)
calories_ran = fitness_tracker.run_calories(ran_km)
calories_cycled = fitness_tracker.cycle_calories(cycled_km)
# # TODO: Sum and print the total calories burned for the day.
print(f"Calories burned walking: {calories_walked}")
print(f"Calories burned running: {calories_ran}")
print(f"Calories burned cycling: {calories_cycled}")

total_calories = calories_walked + calories_ran + calories_cycled
print(f"Total calories burned today: {total_calories}")
# #------------------------------------------------------------------------------------
# # Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# # TODO: Ask the user to input the total loan amount.
loan_amount = float(input("Enter the total loan amount: "))
# # TODO: Ask the user to input their monthly repayment amount.
monthly_payment = float(input("Enter your monthly payment amount: "))
# # TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
while loan_amount > 0:
    loan_amount -= monthly_payment
    if loan_amount < 0:
        loan_amount = 0
  
# # TODO: Print the remaining loan amount after each payment.
print(f"Remaining loan amount: ${round(loan_amount,2)}")
# # TODO: When the loan is fully paid off, print a congratulatory message.
print("Congratulations! You've paid off the loan.")


