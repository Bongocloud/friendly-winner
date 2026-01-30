"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS (Nicole L.)
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Get user input

number_one = int(input(f"\n Enter whole number here: "))
number_two = int(input(f" Enter another whole number: "))



# Use the numbers for logical checks (, Not Zero)

if number_one > 100 and number_two > 100:
    print(f"\n Both are greater than 100!")
else: 
    print(f"\n Both are not greater than 100.")

if number_one % 2 == 0 or number_two % 2 == 0:
    print(f"\n One or both are even numbers.")
else: 
    print(f"\n Neither are even.")

if number_one != 50 or number_two != 50:
    print(f"\n One of these is not equal to 50.")
else: 
    print(f"\n Both are even to 50!")

if number_one < 100 or number_two < 100:
    print(f"\n One or both are less than 100")
else: 
    print(f"\n Both are greater than 100")

if number_one > 0 and number_two > 0:
    print(f"\n Both numbers are greater than 0!")
else: 
    print(f"\n")

if not (number_one == 0):
    print(f"\n Is Zero")
else: 
    print(f"\n Not Zero")

# Categorize number_one (Positive/Negative/Zero)

print(f"\n Categorizing first number")

if number_one > 0:
    print(f"\n Positive")
elif number_one < 0:
    print(f"\n Negative")
else:
    number_one == 0
    print(f"\n Zero")