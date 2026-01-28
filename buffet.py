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

#Determine price and show the user

if age >= 65:
    print(f"\n Your price is $12.95 due to senior discount")
    if age >= 12:
        print:f"\n You must pay the standard $16.95"
    else:
        print:(f"\n Determining... Please Wait")
else:
    if age > 1:
        print(f"\n You must pay ${age:,.2f}")
    else:
        print(f"\n Those under 1 don't have to pay, the price is $0.00.")