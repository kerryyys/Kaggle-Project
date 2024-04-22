#You are tasked to code the vending machine logic out using Python Programming Language. In your code, you can have a few drinks as your items with any price (no coin). The customer should be able to insert any notes to buy his preferred drinks. The outcome is to release the least amount of notes back to the customer. 

# Drinks
drinks = {
    '1': {'name': 'Coca Cola', 'price': 5.00},
    '2': {'name': 'Pepsi', 'price': 4.00},
    '3': {'name': 'Sprite', 'price': 3.00},
    '4': {'name': 'Fanta', 'price': 2.00},
    '5': {'name': '7-Up', 'price': 1.00}
}

print("Welcome to XXX Vending Machine!")
print("Please select your drinks:")

for key, value in drinks.items():
    print(f"{key}. {value['name']} - RM{value['price']}")

selected_drinks = []

print
while True:
    # Get user input
    selection = input("Enter your choices (separated by spaces, or 'done' to finish): ")

    # Check if user is done selecting
    if selection.lower() == 'done':
        break

    choices = selection.split()

    valid_selections = [choice for choice in choices if choice in drinks]
    invalid_selections = [choice for choice in choices if choice not in drinks]

    if invalid_selections:
        print(f"Invalid selections: {', '.join(invalid_selections)}")

    selected_drinks.extend([drinks[choice] for choice in valid_selections])

#Count total amount of drinks and initialize user total payment
total_amount = sum(drink['price'] for drink in selected_drinks)
total_payment = 0

print(f"Total price: RM{total_amount}")

#Check user payment 
while True:
    payment = float(input("Enter the total amount: "))
    total_payment += payment
    # Check if the total amount matches the calculated total
    if total_payment < total_amount:
        print(f"Not enough. Insert RM{total_amount - total_payment} more.")
    else:
        break

# Calculate and display change for each selected drink
change = total_payment - total_amount
print("Thank you for purchasing the following drinks:")
for drink in selected_drinks:
    print(f"{drink['name']}")

print(f"Total change: RM{change:.2f}")

# Calculate the number of each note to return
notes = [100, 50, 20, 10, 5, 1]
return_notes = []

for note in notes:
    count = int(change // note)
    if count > 0:
        return_notes.append(f"{count} x RM{note}")
        change -= count * note

if return_notes:
    print("Return to you:")
    for note in return_notes:
        print(note)
else:
    print("No return notes needed.")
