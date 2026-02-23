"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

magic_ball = True

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later.","I don't think so","Not in this lifetime.","Next year","Indubitably","Depends on the details")

print("Welcome to the Digital Oracle!")

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop
while magic_ball == True:
    user_input = input(f"\nType in your question: \n")
    clean_input = user_input.strip().lower()
    if  clean_input == "quit":
        print (f"\n Goodbye!")
        magic_ball = False
    else: 
        print(random.choice(RESPONSES))

 