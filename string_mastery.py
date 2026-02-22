"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: [Nicole L.]
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"
# TODO: Print the length of 'instrument'
print(len(instrument))
# TODO: Print the first and last letter of 'instrument'
print(instrument[0])
print(instrument[14])
# TODO: Use min() and max() to find and print the lowest and highest ASCII characters
print(min(instrument))  
print(max(instrument)) # Struggling a bit on the min/max function as I can't get the first one to show


# --- TASK 2: THE CLEANUP CREW 🧵 ---
messy_input = "   vOLUME_knob_11   "
# TODO: Use .strip() to remove spaces
# TODO: Use .upper() to capitalize everything
# TODO: Use .replace() to swap the underscores "_" for spaces " "
print(messy_input.strip().upper().replace("_", " "))

# --- TASK 3: THE VALIDATOR 🔍 ---
serial_number = "90210"
# TODO: Use .isdigit() to check validity.
# Print "Valid Serial" if it is numeric, or "Invalid Serial" if it isn't.
if serial_number.isdigit():
    print(f"\nValid Serial")
else:
    print(f"\nInvalid Serial")

# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")

# TODO: Create a loop that iterates through name_string (for char in name_string)
# TODO: Inside the loop:
for char in name_string:
#       1. Use " ".join(duck_letters) to create a variable named 'current_name'
    current_name = " ".join(duck_letters)
#       2. Print: "There was a teacher who had a duck and Ducky was his Name-o"
    print(f"\n There was a teachers who had a duck and Ducky was his Name-o")
#       3. Print the line f"({current_name}) \n" multiplied by 3
    print(f"({current_name}) \n" * 3)
#       4. Print "and Ducky was his Name-o!\n"
    print(f"\n and Ducky was his Name_o! \n")
#       5. Replace the letter in duck_letters at index [count] with "🦆" 
    duck_letters[count] = "🦆"
#       6. Increment count by 1
    count += 1
    
# TODO: After the loop, print the "Finale" (the final version with all 🦆 emojis)
# Hint: You'll need one more .join() and one more print block here!
duck_finale = " ".join(duck_letters)
print(f"({duck_finale}) \n" * 3)
print (f"\n and Ducky was his Name_o! \n")