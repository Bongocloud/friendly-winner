"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# (Nagging Kid) While loop and exit

bored = True

while bored:
       print(f"\n Are we there yet?")

       answer = input("yes/no: ")
       if answer == "yes":
              bored = False


# (99 Bottles of Beer) For loop

for i in range(99, 0, -1):
       print(f"\n {i} bottles of beer on the wall!")