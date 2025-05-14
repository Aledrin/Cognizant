
inventory = {
    "grapes": (15, 1.5),
    "peach": (25, 3),
    "banana": (35, 2),
    "strawberry":(45, 2.5)
}


#add an item
def add_item():
    item_name = input("Enter item name to add: ").strip().lower()
    if item_name in inventory:
        print(f"{item_name} already exists. Use 'Update item' to change it.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[item_name] = (quantity, price)
        print(f"{item_name} added successfully.")
    except ValueError:
        print("Invalid input. Quantity must be an integer and price must be a number.")

#remove an item
def remove_item():
    item_name = input("Enter item name to remove: ").strip().lower()
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed successfully.")
    else:
        print(f"{item_name} not found in inventory.")

#update an item
def update_item():
    item_name = input("Enter item name to update: ").strip().lower()
    if item_name in inventory:
        try:
            quantity = int(input("Enter new quantity (or -1 to keep current): "))
            price = float(input("Enter new price (or -1 to keep current): "))
            current_quantity, current_price = inventory[item_name]
            new_quantity = quantity if quantity != -1 else current_quantity
            new_price = price if price != -1 else current_price
            inventory[item_name] = (new_quantity, new_price)
            print(f"{item_name} updated successfully.")
        except ValueError:
            print("Invalid input. Quantity must be an integer and price must be a number.")
    else:
        print(f"{item_name} not found in inventory.")

#Display the Inventory
def display_inventory():
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, (quantity, price) in inventory.items():
            print(f"Item: {item.capitalize()}, Quantity: {quantity}, Price: ${price}")
    print("--------------------------")

# Calculate Total Value
def calculate_total_value():
    total = sum(quantity * price for quantity, price in inventory.values())
    print(f"\nTotal value of inventory: ${total}")

# Menu
def menu():
    while True:
        print("\nInventory Manager - Menu")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Calculate Total Value")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            calculate_total_value()
        elif choice == '6':
            print("Exiting Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")
print("Welcome to Inventory Manager!")
menu()