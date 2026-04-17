#!/usr/bin/env python3
"""Mini project CLI: cafe menu and basket management"""

#######basket ammar and jacob
#####just testing a 2nd commit to my branch
def print_basket_menu():
    print("\nBasket Options")
    print("1 - View Basket")
    print("2 - Remove Item from Basket")
    print("3 - Clear Basket")
    print("0 - Back to main menu")

def handle_basket_menu(basket):
    while True:
        print_basket_menu()
        choice = get_choice("Select main option", {"0", "1", "2", "3"})

        if choice == "0":
            break
 
        elif choice == "1":
            display_items(basket, "Items in your basket")
 
        elif choice == "2":
            if not basket:
                print("Your basket is empty")
                continue
            display_items(basket, "Select item to remove")
            idx = get_numeric_choice("Enter collerating index to remove", 0, len(basket) -1)  
            removed = basket.pop(idx)
            print(f"Removed '{removed}' from your basket.")  
 
        elif choice == "3":
            if confirm("Are you you want to clear the entire basket? (y/n)"):
                basket.clear()
                print("Basket Cleared.")
            
 
def print_main_menu():
    """Display the main menu options."""
    print("\nMAIN MENU")
    print("1 - Cafe menu")
    print("2 - Add new item to cafe menu")
    print("3 - Edit cafe menu")
    print("4 - View/Manage Basket")
    print("0 - Exit")
 
 
def print_cafe_menu(cafe_items):
    """Display the cafe menu with numbered items."""
    print("\nCAFE MENU")
    if not cafe_items:
        print("(no items available)")
    else:
        for idx, item in enumerate(cafe_items, 1):
            print(f"{idx} - {item}")
    print("0 - Back to main menu")
 
 
def print_edit_menu():
    """Display the edit menu options."""
    print("\nEDIT CAFE MENU")
    print("1 - Update item name")
    print("2 - Remove item")
    print("0 - Back to main menu")
 
 
def get_choice(prompt, valid_options):
    """Prompt until user chooses one of valid options."""
    valid_str = ", ".join(sorted(valid_options))
    while True:
        choice = input(f"{prompt} ({valid_str}): ").strip().lower()
        if choice in valid_options:
            return choice
        print(f"Invalid choice. Choose {valid_str}.")
 
 
def get_valid_index(items, prompt):
    """Prompt for a valid index within the items list."""
    while True:
        idx_input = input(f"{prompt} (0-{len(items)-1}): ").strip()
        if not idx_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        idx = int(idx_input)
        if idx < 0 or idx >= len(items):
            print("Index out of range.")
            continue
        return idx
 
 
def confirm(prompt):
    """Ask user to confirm yes/no."""
    return get_choice(prompt, {"y", "n"}) == "y"
 
 
def get_numeric_choice(prompt, minimum, maximum):
    """Prompt for numeric choice inside range."""
    while True:
        value = input(f"{prompt} ({minimum}-{maximum}): ").strip()
        if not value.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        num = int(value)
        if num < minimum or num > maximum:
            print("Number out of range.")
            continue
        return num
 
 
def display_items(items, title):
    """Display a list of items with indices."""
    print(f"\n{title}:")
    if not items:
        print("(none)")
    else:
        for idx, item in enumerate(items):
            print(f"{idx}: {item}")
 
 
def handle_cafe_menu(cafe_items, basket):
    """Handle the cafe menu for ordering."""
    while True:
        print_cafe_menu(cafe_items)
        if not cafe_items:
            choice = get_choice("No items to select, enter 0 to return", {"0"})
            if choice == "0":
                break
            continue
 
        selected = get_numeric_choice("Select item number to add to basket", 0, len(cafe_items))
        if selected == 0:
            break
 
        item = cafe_items[selected - 1]
        if confirm(f"Add '{item}' to basket? (y/n)"):
            basket.append(item)
            print(f"'{item}' added to basket.")
        else:
            print("Not added.")
 
 
def handle_add_item(cafe_items):
    """Handle adding a new unique item to the cafe menu."""
    new_item = input("Enter new cafe item name: ").strip()
    if new_item:
        if new_item in cafe_items:
            print(f"'{new_item}' is already in the cafe menu.")
        else:
            cafe_items.append(new_item)
            print(f"'{new_item}' added to cafe menu.")
    else:
        print("No item name entered.")
 
 
def handle_edit_menu(cafe_items):
    """Handle the edit menu for updating or removing items."""
    while True:
        print_edit_menu()
        edit_choice = input("Select edit option: ").strip()
 
        if edit_choice == "0":
            break
 
        elif edit_choice == "1":
            if not cafe_items:
                print("No items to update.")
                continue
            display_items(cafe_items, "Current cafe items")
            idx = get_numeric_choice("Enter index to update", 0, len(cafe_items) - 1)
            new_name = input("Enter new name: ").strip()
            if new_name:
                old_name = cafe_items[idx]
                cafe_items[idx] = new_name
                print(f"Updated '{old_name}' to '{new_name}'")
            else:
                print("No new name entered.")
 
        elif edit_choice == "2":
            if not cafe_items:
                print("No items to remove.")
                continue
            display_items(cafe_items, "Current cafe items")
            idx = get_numeric_choice("Enter index to remove", 0, len(cafe_items) - 1)
            removed = cafe_items.pop(idx)
            print(f"Removed '{removed}' from cafe menu.")
 
        else:
            print("Invalid edit menu choice.")
 
################# ORDER FUNCTIONS #################



################# MAIN APPLICATION LOOP #################
def main():
    """Main application loop."""
    cafe_items = ["Coffee", "Tea", "Latte", "Cappuccino", "Sandwich", "Cake", "Muffin", "Bagel"]
    basket = []
 
    while True:
        print_main_menu()
        choice = get_choice("Select main option", {"0", "1", "2", "3", "4"})
 
        if choice == "0":
            print("Goodbye.")
            break
 
        elif choice == "1":
            handle_cafe_menu(cafe_items, basket)
 
        elif choice == "2":
            handle_add_item(cafe_items)
 
        elif choice == "3":
            handle_edit_menu(cafe_items)
        
        elif choice == "4":
            handle_basket_menu(basket)
 
 
 
if __name__ == "__main__":
    main()
 



