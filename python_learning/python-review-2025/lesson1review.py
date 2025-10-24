#Part one: For each line of code below, write what type of variable is being stored (string, integer, or float). Write your answer as a comment next to each line of code.

first_name = "Bro" # for example: this is a string
food = "pizza"
email = "Bro123@fake.com"
age = 25
quantity = 3
price = 10.99
gpa = 3.2
distance = 5.5

#Part 2 – Predict the Output

#Without running the code, predict what each line will print:
print(f"Hello {first_name}") # for example: Hello Bro
print(f"You like {food}") # for example: You like pizza
print(f"Your email is: {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")


# Part 3 – Fix the Errors

# The following code has two mistakes.
# Find and fix them so it runs correctly.

name = "Bro"        
food = "pizza"        
print(f"Hello {name}") 
print (f"You like {food}")
# Missing quotes and wrong variable name
# food = pizza
# print(f"You like {favorite_food}")

food = "pizza"        # Added quotes
favorite_food = food   # Define favorite_food or use food directly
print(f"You like {favorite_food}")

# Wrong f-string format
age = 17
print(f"You are {age} years old")  # Added f before string

# Mismatched parentheses
price = 12.99
print(f"The total price is ${price}")  # Added missing closing parenthesis

# Variable name spelled incorrectly
name = "Bro"
print(f"Hello {name}")  # No change needed here, just noting correctness

# Using + instead of commas (no + in provided example, but showing correct usage)
name = "Bro"
print(f"Hello {name}")  # Use f-string, no commas or + needed here

# Mixing single and double quotes incorrectly
email = "Bro123@fake.com"  # Corrected quotes to match
print(f"Your email is: {email}")

# Forgot to include the f before the string
age = 21
print(f"You are {age} years old")  # Added f
# Trying to use a number as a variable (no code provided here but explanation given)
cool = "yes"
print(f"Am I cool? {cool}")

#rules for variable names state that they
#cannot start with a number 
#another rule is that variable names cannot have space
#another rule is that variable names
#cannot have special characters like !,@,#,$,%,^,&,*,(,)
#cannot use reserved keywords like class,def,return,etc.
# Missing curly braces
quantity = 3
print(f"You are buying {quantity} items")  # Added space and braces correct

# Using a reserved keyword
# Using a reserved keyword
class_3 = "ECS"
print(f"You are in {class_3}")



# Part 4 – Create Your Own

# Write a short Python program that:

# Creates at least three variables (a string, an integer, and a float)

# Prints a formatted message using f-strings that combines all three.
#  Example:
movie = "Inception"
rating = 9.5
year = 2006
print(f"My favorite movie is {movie}, released in {year}, rated {rating}/10!")

movie = "cars"
rating = 9.5
year = 2010
print(f"My favorite movie is {movie}, released in {year}, rated {rating}/10!")

