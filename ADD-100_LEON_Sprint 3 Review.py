""" 
Assignemnt 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Energy Outlet
Developer: Nicole Leon
"""

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
    # TODO: Form loop that repeatedly asks user wether they want to add another drink to the oder until "N" is entered.
    return "N"

def calculate_price(drink_choice):
    """Grab corresponding drink price from PRICE_FILE for total calculations.
    ensure the price is shown as a float & put through try/except ValueError."""
    return 2.50
    # TODO: Grabs price of drinks from PRICE_FILE file and calculates the end total of the order.

def customer_history(user_name, final_price):
    """ Appends to order_history.txt and prints human-readable label."""
    # TODO: Write data for computer and receipt format for customer
    pass


def main():
    # 1. Customer Info
    name = customer_name()
    print (f"Name: {name}")

    # 2. Data Collection
    brand, drink = choose_brand(), drink_choice()
    print(f"Drink: {drink}")

    # 3. Price Calculations
    final_price = calculate_price(drink_choice=drink) 
    print(f"Total: {final_price:.2f}")

    # 4. Customer History
    customer_history(user_name=name, final_price=final_price)

main()