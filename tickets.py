"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# Seating list

seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

choosing = True

# print and get seat selection

while choosing == True:
    print(f"\n Seats {seats} are available.")
    seat_selection = int(input(f"\n Select One of the options (1-20). Selecting 0 will end this program: "))

    if seat_selection == 0:
        print(f"\n Goodbye!")
        choosing = False

    elif seat_selection in seats:
        seats.remove(seat_selection)
        print(f"\n The seat is now yours!")

    else:
        print(f"\n Seat is taken")  