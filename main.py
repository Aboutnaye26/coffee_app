import time


def display_menu():
    print("Welcome to our Coffee Shop!")
    print("Please choose your coffee:")
    print("1. Americano - $3.00")
    print("2. Latte - $3.50")
    print("3. Cappuccino - $4.00")
    print("4. Espresso - $2.50")
    print("5. Finish order")
    # This is the entire menu


def get_coffee_choice():
    choices = []
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice in ['1', '2', '3', '4']:
            choices.append(int(choice))
            print("Added to order. You can add more or finish your order.")
        elif choice == '5':
            if choices:
                return choices
            else:
                print("You haven't added any coffees to your order. Please add at least one coffee.")
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")


def get_topping_choices():
    print("\nWould you like to add any toppings? (Enter 'done' when finished)")
    print("1. Extra Cream - $0.50")
    print("2. Milk - $0.80")
    print("3. Sugar - $0.70")
    toppings = []
    while True:
        choice = input("Enter your choice (1-3 or 'done'): ")
        if choice in ['1', '2', '3']:
            toppings.append(int(choice))
        elif choice.lower() == 'done':
            return toppings
        else:
            print("Invalid choice. Please choose a number between 1 and 3 or 'done'.")
