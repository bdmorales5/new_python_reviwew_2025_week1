# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")


#get user name
name=input("what is your name?")
#this is input always a string
print(f"Hi {name}! lets do some math.\n")
#is your output

#ask for birthday and favorite food and two numbers

birthday=input("when is your birthday?")

favorite_food=input("whats your favorite food?")

print(f"cool! your birthday is {birthday}, And you like {favorite_food}")
num1= input("enter first number")
num2= input ("enter second number")

num1= float(num1)
num2= float(num2)
print(f"the numbers you enter are {num1}, And {num2}")


print(f"cool! your birthday is {birthday}, And you like {favorite_food}")
print(f"the numbers you enter are {num1}, And {num2}")
print(f"the sum of {num1} and {num2} is {num1 +num2}.")
# Get two numbers from the user and ask for their name to personalize the experience


















# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings