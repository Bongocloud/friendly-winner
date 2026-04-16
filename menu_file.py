"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

# "with" statement opens and closes files automatically
# "a" = Append to a text file (Adds new data to the end), "r" = Read from a text file (File must exist)
# Run Try/Except block


def file_read():
    menu_data = {}
    try:
        with open("menu_config.txt", "r") as file:
            for line in file:
                category, detail = line.strip().split(",")
                menu_data[category] = detail     
    except FileNotFoundError:
        print(f"Error: menu_config.txt NOT found")

    return menu_data

def main():

    my_menu = file_read()
    menu_category = my_menu.get("Food", "Not Found")

    # For loop
    for category, detail in my_menu.items():
        print(f"{category}: {detail}")

main()