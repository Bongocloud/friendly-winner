"""
ASSIGNMENT 11B: SPRINT 4 - WRITING TO FILES
Project: Energy Outlet
Developer: Nicole Leon
"""

import datetime

# GLOBAL CONSTANTS (Pantry Rules)
OPTION_FILES = "monster.txt", "redbull.txt", "celcius.txt", "reign.txt", "cfour.txt"


def customer_name():
    """ Asks for customer's name."""
    # TODO: Ask for name, and print name. 
    return "Nicole"

def choose_brand():
    """ Ask customer to choose a brand, check input, grab corresponding file USE: .strip.upper ."""
    # TODO: Ask for brand choice, check the input make sure it's valid.
    return "Monster"

def drink_choice():
    """ Ask for the type of drink from the brand 
    (shows selection based on brand choice). USE: .strip.upper ."""
    # TODO: Load drink options from selected OPTION_FILES, get customer choice, Run validation for input.
    return "Mango Loco"

def loop_questions():
    """ Loop the questions and add to the order if customer selects more,
    if "N" end loop and confirm selection(s)."""
    # TODO: Form loop that repeatedly asks user wether they want to add another drink to the order until "N" is entered.
    return "N"

def calculate_price(brand_choice, drink_choice):
    """Grab corresponding drink price from price_file for total calculations.
    ensure the price is shown as a float & put through try/except ValueError."""
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
    # TODO: Grabs price of drinks from PRICE_FILE file and calculates the end total of the order.

def customer_history(user_name, final_price):
    """ Appends to order_history.txt and prints human-readable label."""
    # TODO: Write data for computer and receipt format for customer
    timestamp = datetime.datetime.now()

    try:
        with open("order_history.txt", "a") as history_file:
            history_file.write(f"----Customer History----\n")
            history_file.write(f"{user_name}, {final_price:.2f}, {timestamp}\n")
    except Exception as e:
        print(f"System Error: {e}")


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