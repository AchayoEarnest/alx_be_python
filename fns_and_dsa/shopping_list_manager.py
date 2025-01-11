#!/usr/bin/env python3

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter an item to add in your shopping list: ").strip()
            shopping_list.append(item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter an item to remove from your shopping list: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item}, removed from the list.")
            else: 
                print(f"'{item}', not found in the list.")
            # pass
        elif choice == '3':
            # Display the shopping list
            print("\nShopping list:")
            if shopping_list:
                for idx, items in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                else:
                    print("The list is empty.")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()