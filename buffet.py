"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [1/28/2025]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

# Get user age information
age = int(input("Enter your age here: "))

# Price options:

age_price = age 
standard_price = 16.95
senior_discount = 12.95

# Determine price and show the user

if age < 1:
    print(f"\n Those under 1 don't have to pay.")
    print(f"\n Have a good day!")
elif age <= 11:
        print(f"\n You must pay ${age_price:,.2f}")
        print(f"\n Have a good day!")
elif age <= 64:
    print(f"\n You must pay the standard ${standard_price:,.2f}")
    print(f"\n Have a good day!")
else:
    if age >= 65:
        print(f"\n Your price is ${senior_discount:,.2f} due to senior discount")
        print(f"\n Have a good day!")
    else:

        print(f"\n Something went wrong!")
