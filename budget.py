"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f).
-----------------------------------------------------------------------
"""

# Get user's monthly Income info
# Info on how much is spent monthly and for what

monthly_income = float(input("Enter your monthly income here: $"))
monthly_groceries = float(input("How much was spent on groceries this month: $"))
home_bills = float(input("Enter your monthly pay for home bills (gas, electricity,water, etc.): $"))
monthly_car_payments = float(input("Insert your monthly car payment amount: $"))
monthly_phone_service = float(input("Enter payment amount for phone service this month: $"))
monthly_entertainment = float(input("Enter monthly pay for entertainment subscriptions: $"))

# Calculate percentage of monthly Income spent

total_spent = monthly_groceries + home_bills + monthly_car_payments + monthly_phone_service + monthly_entertainment
percent_spent = total_spent / monthly_income
percent_spent = percent_spent * 100

# Calculate money left to spend

money_left = monthly_income - total_spent

# Print total spent, percentage spent, and how much is left to pend

print (f"\n -----------TOTAL SPENT----------- ")
print (f"\n Groceries:                    ${monthly_groceries:,.2f}")
print (f" Bills:                        ${home_bills:,.2f}")
print (f" Car Payments:                 ${monthly_car_payments:,.2f}")
print (f" Phone Service:                ${monthly_phone_service:,.2f}")
print (f" Entertainment Subscription:   ${monthly_entertainment:,.2f}")
print (f" Total:                        ${total_spent:,.2f}")
print (f"\n -----------------------------------")
print (f" -----PERCENTAGE OF INCOME SPENT-----")
print (f"\n Percentage of income lost:  %{percent_spent:,.2f}")
print (f"\n -----------------------------------")
print (f" -----------LEFT TO SPEND-----------")
print (f"\n You have:                   ${money_left:,.2f} left to spend.")
