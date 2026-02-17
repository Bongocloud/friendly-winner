"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""
# months as constant tuple
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Display and modify

for all_months in MONTHS:
    print(f"\n These are the months: {all_months}.")
    print(f"\n Modifying Month")
    try:
        MONTHS[0] = "Snail"
    
    except TypeError:
        print(f"\n ERROR: Month cannot be changed!")

# Months could not be changed as they are immutable due to being placed in a Tuple. 
# Since the system will not allow the change, trying to make one will have the code fail as it is not useable.
# The TypeError handles the change by detecting and letting the person know 
# that it cannot be changed and then closing instead of crashing.