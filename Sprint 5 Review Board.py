"""
ASSIGNMENT 13A: SPRINT 6 Review Board
Project: Energy Outlet
Developer: Nicole Leon
"""

import datetime


# GLOBAL CONSTANTS (Pantry Rules)
OPTION_FILES = "monster.txt", "redbull.txt", "celcius.txt", "reign.txt", "cfour.txt"
USER_HISTORY = "order_history.txt"

def customer_name():
    """ Asks for customer's name."""
    # TODO: Ask for name, and print name. 
    customer = input(f"Please enter your name here: ").strip()
    return customer

def choose_brand():
    """ Ask customer to choose a brand, check input, grab corresponding file USE: .strip.upper ."""
    # TODO: Ask for brand choice, check the input make sure it's valid.
    brand = input(f"Choose a brand (Monster, Redbull, Celcius, Reign, C4): ").strip().capitalize()
    return brand

def drink_choice():
    """ Ask for the type of drink from the brand 
    (shows selection based on brand choice). USE: .strip.upper ."""
    # TODO: Load drink options from selected OPTION_FILES, get customer choice, Run validation for input.
    drink = input(f"Enter what drink you would like {OPTION_FILES}")
    return drink

def loop_questions():
    """ Loop the questions and add to the order if customer selects more,
    if "N" end loop and confirm selection(s)."""
    # TODO: Form loop that repeatedly asks user wether they want to add another drink to the order until "N" is entered.
    return "N"

def calculate_price(brand_choice, drink_choice):
    # Grabs corresponding drink price from price_file for total calculations.
    # Ensure the price is shown as a float & put through try/except ValueError.
    try:
        with open(f"{brand_choice.lower().strip()}.txt", "r") as drink_file:
            for line in drink_file:
                drink_request, drink_price = line.strip().split(",")
                if drink_request.upper().strip() == drink_choice.upper().strip():
                    return float(drink_price), "Price Grabbed!"
    except FileNotFoundError:
        """ Make universal safetynet. """
        return float(0.00), "Drink not found"
    return float(0.00), "Drink not found"

def customer_history(user_name, final_price):
    """ Appends to order_history.txt and prints human-readable label."""
    # TODO: Write data for computer and receipt format for customer
    timestamp = datetime.datetime.now()

    """Writes the user history into the history file"""
    try:
        with open("order_history.txt", "a") as history_file:
            history_file.write(f"{user_name}, {timestamp}, ${final_price:.2f}\n")
    except Exception as e:
        print(f"System Error: {e}\n")


def edit_history_file():
    """Reads the file and lets the user modify or change there input"""
    
    try: 
        records = []
        with open("order_history.txt", "r") as read_file:
            for line in read_file:
                user_name, timestamp, final_price  = line.strip().split(",")
                records.append([user_name, timestamp, final_price])
        for index, item in enumerate(records):
                print(f"ID: {index},Name: {item[0]}, Date: {item[1]}, Price: {item[2]}\n")
                      
    except FileNotFoundError:
        print(f"ERROR: File was not found!\n")         

        """Allow user to change any part of the record"""
    try:
        edit_request = int(input(f"Which ID number would you like to edit?: \n"))
        if edit_request not in records:
            print(f"ID not found. Try again.")

        edit_made = input(f"What is the new name for {edit_request}?: \n")
        records[edit_request] = edit_made
        print(f"Update Succesful!\n")

    except ValueError:
        print(f"Invalid input: Please enter a numeric ID.")
    

    try:        
        with open("order_history.txt", "w") as write_file:
            for record in records:
                write_file.write(f"{record[0]},{record[1]},{record[2]}\n")
    except TypeError as e:
        print(f"TypeError occured: {e}\n")
        

def receipt(user_name, final_price, timestamp):
    """Receipt shows final receipt"""
    try:
        with open("receipt.txt", "w") as receipt_file:
                receipt_file.write(f"---------Energy Outlet---------\n")
                receipt_file.write(f"-------------------------------\n")
                receipt_file.write(f"Name: {user_name}\n")
                receipt_file.write(f"Date: {timestamp}\n")
                receipt_file.write(f"-------------------------------\n")
                receipt_file.write(f"   TOTAL: ${float(final_price):.2f}\n")
                receipt_file.write("------Enjoy your beverage!------\n")
    except Exception as e:
        print(f"Error printing receipt: {e}")
    

def main():

    continue_program = input(f"Enter 'Y' to add another drink, or 'N' to stop: ").strip().upper()
    while continue_program == "Y":

        # 1. Customer Info
        name = customer_name()
        print (f"Name: {name}")

        # 2. Data Collection
        brand, drink = choose_brand(), drink_choice()
        print(f"Drink: {drink}")

        # 3. Price Calculations, 4. Customer History
        try:
            final_price, status = calculate_price(brand_choice=brand, drink_choice=drink) 
            print(f"Total: {final_price:.2f}")
            customer_history(user_name=name, final_price=final_price)
        except ValueError:
            print("Error: Could not process price.")
        
        
        print(f"\n ")

        continue_program = input(f"Enter 'Y' to add another drink, or 'N' to stop: ").strip().upper()

main()