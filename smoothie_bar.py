"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

 # GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

 # TODO: Define get_price(size)
def base_price(size):
 #size prices
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00

 # TODO: Define blend(size, base, fruit, scoops)
def smoothie_blend (size, BASES, FRUITS, scoops):
    print (f"\n---Smoothie Bar---")
    print (f"\nSize: {size}")
    print (f"Base: The smoothie will have a(n) {BASES} base.")
    print (f"Fruit: {FRUITS} added.")
    print (f"Scoops: {scoops} scoops of {FRUITS}.")
   

 # TODO: Define main() to collect input and call your logic
def main():
    print (f"\nThis is the Smoothie Bar, WELCOME!")
    get_size = input(f"Size Options: (Small/Medium/Large): ").title().strip()
    get_base = input(f"Choose a Base: ")
    get_fruits = input (f"Choose fruit: ")
    
    try: 
        get_scoops = int(input(f"How many scoops of fruit?: "))
    except ValueError:
        print("Invalid Input, Defualting to 1 scoop.")
        get_scoops = 1

 # Getting the price and smoothie blend function.
    cost = base_price(get_base)
                      
    smoothie_blend(get_size, get_base, get_fruits, get_scoops)

    print (f"\nTotal Payment: ${cost:.2f}")

 # Run system
main()