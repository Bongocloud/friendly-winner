"""
-----------------------------------------------------------------------
ASSIGNMENT 5B: THE ATM
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. 'while' loop keeps the program running.
[ ] 3. I have handled ValueErrors (Type Safety).
[ ] 4. I have blocked Negative numbers and Overdrafts.
[ ] 5. I have pinned the 'balance' in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

#Set ATM to running, set balance

balance = 1000
running = True

#Show menu, While loop for each selection

while running == True:
    try:
        print(f"\n Menu: 1. Balance, 2. Deposit, 3. Withdraw, 4. Exit")
        menu_select = int(input(f" Select an option from 1-4: "))

    # 1. = Print Balance

        if menu_select == 1:
            print(f"\n Your balance is ${balance:.2f}")

    # 2. = Deposit

        elif menu_select == 2:
            try:
                deposit_amount = float(input(f"\n How much would you like to deposit?: "))
                if deposit_amount < 0:
                    print(f"\n Amount cannot be less than zero!")
                    deposit_amount = float(input(f"\n How much would you like to deposit?: "))
                else:
                    balance = balance + deposit_amount
                    print(f"\n Your balance is now {balance:.2f}")
            except ValueError:
                print(f"\n ERROR: Please enter numbers only!")

    # 3. = Withdraw

        elif menu_select == 3:
            try: 
                withdraw_amount = float(input(f"\n How much would you like to withdraw?: "))
                if withdraw_amount < 0 or withdraw_amount > balance :
                    print(f"\n The amount cannot be less then 0 or greater than ${balance:.2f}!")
                else:
                    balance = balance - withdraw_amount
                    print(f"\n your balance is now {balance:.2f}")
            except ValueError:
                print(f"\n ERROR: Please enter numbers only!")

    # 4. = Exit acc or turn ATM off

        elif menu_select == 4:
            running = False

        else: 
            print(f"\n Invalid please choice a number 1-4")

    except ValueError:
        print(f"\n ERROR: Please enter numbers only!")

        