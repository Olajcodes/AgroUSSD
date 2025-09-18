from models.buyer import Buyer
from models.farmer import Farmer

def main_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ----- Welcome to USSD Digital Marketplace ------ ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("")

def get_pin():
    while True:
        pin = input("Enter your PIN (4 digits): ")
        if pin.isdigit() and len(pin) == 4:
            return pin
        print("Invalid PIN. Please enter exactly 4 numeric digits.")

while True:
    main_menu()
    choice = input("Hello, what would you like to do today? Please select from options 1 to 3: ")

    if not choice.isdigit() or int(choice) not in (1, 2, 3):
        print("Oops! Wrong input. Please enter a number between 1 and 3.")
        continue

    choice = int(choice)

    if choice == 1:
        print("******************************")        
        print("1. Farmer")
        print("2. Buyer")
        print("3. Go back")
        print("======================")
        
        option = input("Enter choice (1/2/3): ")
        if not option.isdigit():
            print("Invalid option. Please enter a number.")
            continue

        option = int(option)

        if option == 1:
            # Farmer registration
            name = input("Enter your fullname: ")
            location = input("Enter your Location (e.g Ibadan): ")
            phone_number = input("Enter your phone number: ")
            pin = get_pin()
            farm_size = input("Enter your farm size (e.g 10 acres): ")
            primary_crop = input("Enter your primary crop (e.g tomato, yam, maize): ")

            farmer = Farmer(name, phone_number, location, pin, farm_size, primary_crop)
            farmer.registration()

        elif option == 2:
            # Buyer registration
            name = input("Enter your fullname: ")
            location = input("Enter your Location (e.g Lagos): ")
            phone_number = input("Enter your phone number: ")
            pin = get_pin()

            buyer = Buyer(name, phone_number, location, pin)
            buyer.registration()

        elif option == 3:
            # Go back to main menu
            continue
        else:
            print("Invalid option, please try again.")

    elif choice == 2:
        # TODO: implement login flow
        print("Login feature coming soon...")

    elif choice == 3:
        print("Goodbye!")
        break
