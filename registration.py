"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# Get user's first and last name
first_name = input("\n Enter First Name: ")
while first_name == "":
    print("ERROR: Name cannot be blank.")
    first_name = input("Please enter First Name: ")

last_name = input("Enter Last Name: ")
while last_name == "":
    print("ERROR: Name cannot be blank.")
    last_name = input("Please enter Last Name: ")

# Ask if user is a chaperone

chaperone = input("\n Parent volunteering to chaperone? (Y/N): ")
while chaperone != "Y" and chaperone != "N":
    print("ERROR: Please enter only Y or N.")
    chaperone = input("Parent volunteering to chaperone? (Y/N): ")

# Ask user's phone number 

phone_number = input("\n Now enter your phone number: ")
while phone_number == "":
    print("ERROR: Number cannot be blank.")
    phone_number = input

print(f"\n Registration and Information complete!")

# Number of tickets needed for finalization
tickets = 0
while True:
    try:
        tickets = int(input("\n How many tickets do you need?: "))
        if tickets > 0:
            break # Valid number, leave loop!
        print ("\n ERROR: Must be at least 1 ticket.")
    except ValueError:
        print("\n ERROR: Please enter a NUMBER (Ex: 1,2,3 etc. NOT 'Five')")

print (f"\n Tickets Ordered: {tickets}")

