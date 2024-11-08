# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruit_list=["apple " , "banana " , "pear " ,"strawberry " , "avocado" ]
# TODO: Add a fruit to the end of the list
fruit_list=["apple " , "banana " , "pear " ,"strawberry " , "avocado" , "guava" ]
# TODO: Insert a fruit at the beginning of the list
fruit_list=["peach " , "apple " , "banana " , "pear " ,"strawberry " , "avocado" , "guava" ]
# TODO: Remove a fruit from the list
fruit_list=["peach " , "apple " , "banana " ,"strawberry " , "avocado" , "guava" ]
# TODO: Print the modified list
print(fruit_list)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
number_list = [1 , 2 , 3 , 4 , 5 ]
# TODO: Create a new list with each number squared
number_squared = [1 , 4 , 9 , 16 , 25 ]
# TODO: Find the sum and average of the original numbers
sum_of_numbers = sum(number_list)

average_of_numbers = sum_of_numbers/len(number_list)

# TODO: Print the results
print(sum_of_numbers) 

print(average_of_numbers)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_capitals = { 
    "France " : " Paris " ,
    " South Africa " : " Pretoria" ,
    " Russia " : " Moscow" ,
    " Germany " : " Berlin " , 
    " Italy " : " Rome " 
}
# TODO: Add a new country-capital pair
countries_capitals = { 
    "France " : " Paris " ,
    " South Africa " : " Pretoria" ,
    " Russia " : " Moscow" ,
    " Germany " : " Berlin " , 
    " Italy " : " Rome " ,
    " China " : " Beijing"
}
# TODO: Update the capital of an existing country
countries_capitals = { 
     "France " : " Paris " ,
    " South Africa " : " Cape Town" ,
    " Russia " : " Moscow" ,
    " Germany " : " Berlin " , 
    " Italy " : " Rome " ,
    " China " : " Beijing"
}
# TODO: Remove a country-capital pair
countries_capitals = { 
     "France " : " Paris " ,
    " Russia " : " Moscow" ,
    " Germany " : " Berlin " , 
    " Italy " : " Rome " ,
    " China " : " Beijing"
}
# TODO: Print the modified dictionary
print(countries_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    " orange " : "orange " ,
    " strawberry " : " red" ,
    " grape " : "purple ",
    " apple " : " green "

}
# TODO: Print all the fruits (keys)
for fruit in fruit_colors.keys() :
    print(fruit)

# TODO: Print all the colors (values)
for color in fruit_colors.values() :
    print(color)

# TODO: Print each fruit and its color
for fruit,color in fruit_colors.items() :
    print(f" {fruit }= {color}")
# TODO: Check if a fruit is in the dictionary and print its color
def check_fruit_color(fruit):
    if fruit in fruit_colors:
        print(f"the color of the {fruit} is {fruit_colors[fruit]}.")
    else:
        print(f"the {fruit} is not found")
check_fruit_color(" grape ")