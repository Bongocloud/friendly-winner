"""Assignment: 9B: SPRINT 2 - Functional Stubs
Project: Energy Outlet
Dev: Nicole
"""

# Constant brand files (Holds all drink options for the brand) (All data within the files can be changed).
OPTION_FILES = "monster.txt", "redbull.txt", "celcius.txt", "reign.txt", "cfour.txt"
PRICE_FILE = "price.txt"

def customer_name():
    """ Asks for customer's name."""
    # TODO: Ask for name, and print name. 
    return "Nicole"

def choose_brand():
    """ Ask customer to choose a brand, check input, grab corresponding file."""
    # TODO: Ask for brand choice, check the input make sure it's valid.
    return "Monster"

def drink_choice():
    """ Ask for the type of drink from the brand 
    (shows selection based on brand choice)."""
    # TODO: Load drink options from selected OPTION_FILES, get customer choice, Run validation for input.
    return "Mango Loco"

def loop_questions():
    """ Loop the questions and add to the order if customer selects more,
    if "N" end loop and confirm selection(s)."""
    # TODO: Form loop that repeatedly asks user wether they want to add another drink to the oder until "N" is entered.
    return "N"

def price_txt(BRAND_PRICE):
    """Grab corresponding price from price.txt for total calculations."""
    # TODO: Grabs price of drinks from price.txt file and calculates the end total of the order.
    pass

def customer_history():
    """ Appends to order_history.txt and prints human-readable label."""
    # TODO: Write data for computer and receipt format for customer
    pass

def main():
    # 1. Customer Info
    name = customer_name
    print (f"Name: {name}")

    # 2. Data Collection
    brand, drink = choose_brand(), drink_choice()
    print(f"{drink_choice}")

    # 3. Price Calculations
    final_price = choose_brand()

    # 4. Customer History
    customer_history(name, final_price)

main()