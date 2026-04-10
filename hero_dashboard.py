"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# Global Constants
TAX_RATE = 0.05
OFFICE_NAME = ("Feel Good Inc.")

def process_expenses(price):
    return price + (price * TAX_RATE), "Complete"

def main():
    try: 
        total = float(input("Enter price: "))
    except ValueError:
        print("INVALID INPUT: Defaulting to 1.00")
        total = 1.00

    total, status = process_expenses(price=total)
    print(f"Total cost is { total:.2f}. The process is {status}.")

main()

