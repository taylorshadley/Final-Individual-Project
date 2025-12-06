# Taylor Shadley
# ISYS 110 Final Individual Project
# Supermarket Catalog
# This program allows the user to browse a supermarket catalog by department,
# view items with prices, add items to a shopping cart, and see a final total.

# -----------------------------------------------------
# Create the data structure (dictionary of items & prices)
# -----------------------------------------------------
supermarket = {
    "Produce": {"Apples": 1.49, "Bananas": 0.59, "Carrots": 2.29, "Lettuce": 1.99},
    "Dairy": {"Milk": 2.99, "Cheese": 4.49, "Yogurt": 0.99, "Butter": 3.29},
    "Bakery": {"Bread": 2.49, "Bagels": 3.99, "Croissants": 4.59, "Muffins": 3.49},
    "Frozen": {"Pizza": 6.99, "Ice Cream": 4.99, "Veggies": 2.79, "Waffles": 3.19},
    "Meat": {"Chicken": 5.49, "Ground Beef": 6.29, "Pork Chops": 5.99, "Turkey": 7.49},
    "Drinks": {"Water": 1.00, "Soda": 2.49, "Juice": 3.29, "Tea": 2.19}
}

# Shopping cart list (stores tuples: (item, price))
cart = []

print("=== Welcome to the Supermarket Catalog ===")

# -----------------------------------------------------
# Main loop for browsing and shopping
# -----------------------------------------------------
while True:
    print("\nAvailable Departments:")
    print("------------------------")
    for dept in supermarket:
        print(f"- {dept}")

    print("\nType 'cart' to view your cart")
    print("Type 'exit' to finish shopping")

    choice = input("\nEnter a department name: ").title()

    # Exit program
    if choice == "Exit":
        break

    # View shopping cart
    if choice == "Cart":
        print("\n=== Your Shopping Cart ===")
        print("------------------------")
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            for item, price in cart:
                print(f"- {item} ..... ${price:.2f}")
        continue

    # Validate department
    if choice not in supermarket:
        print("Invalid department. Please try again.")
        continue

    # Show items with prices
    print(f"\nItems in {choice}:")
    print("------------------------")
    for item, price in supermarket[choice].items():
        print(f"- {item}: ${price:.2f}")

    # Add item to cart
    selected_item = input("\nEnter an item to add to cart (or 'back' to return): ").title()

    if selected_item == "Back":
        continue

    # Validate item
    if selected_item not in supermarket[choice]:
        print("Invalid item. Returning to main menu.")
        continue

    # Add to cart
    cart.append((selected_item, supermarket[choice][selected_item]))
    print(f"{selected_item} has been added to your cart!")

# -----------------------------------------------------
# Final receipt and total cost
# -----------------------------------------------------
print("\n=== FINAL RECEIPT ===")
print("------------------------")

total = 0

if len(cart) == 0:
    print("You did not purchase anything.")
else:
    for item, price in cart:
        print(f"- {item}: ${price:.2f}")
        total += price

print(f"\nTOTAL: ${total:.2f}")
print("\nThank you for shopping!")

# -----------------------------------------------------
# AI Assistance Acknowledgment
# -----------------------------------------------------
print("\n--- AI Assistance Acknowledgment ---")
print("ChatGPT helped with organizing the program and adding the cart + price system.")
