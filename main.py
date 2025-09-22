from models.buyer import Buyer
from models.farmer import Farmer
from models.login import login_user

def main_menu():
    code = input("Dial *222# to access the platform: ")
    while True:
        try:
            if code != "*222#":
                print("Invalid code. Kindly Try Again!")
                code = input("Dial *222# to access the platform: ")
            else: 
                RED = '\033[91m'
                END = '\033[0m'
                title = "Welcome to Farm2Market"
                print("~" *50)
                print(f"\033[1m {RED} {title:^50} {END}")
                print("~" *50)
                print("1. Register")
                print("2. Login")
                print("3. Exit")
                break
        except Exception as e:
            print("Unexpected Error: ", e)

def get_pin():
    while True:
        pin = input("Enter your PIN (4 digits): ")
        if pin.isdigit() and len(pin) == 4:
            return pin
        print("Invalid PIN. Please enter exactly 4 numeric digits.")

while True:
    main_menu()
    choice = input("Hello, what would you like to do today? Please select from options 1 to 3 above: ")

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
            name = input("Hello. Kindly tell us your name: ")
            location = input("What is your location: ")
            phone_number = input("Enter your phone number: ")
            pin = get_pin()
            farm_size = input("How large is your farm in plots? (e.g 4 plots): ")
            primary_crop = input("What are your primary crops?: ")

            farmer = Farmer(name, phone_number, location, pin, farm_size, primary_crop)
            farmer.registration()

        elif option == 2:
            # Buyer registration
            name = input("Hi! Please tell us your fullname: ")
            location = input("Kindly enter your Location (e.g Lagos): ")
            phone_number = input("Please enter your phone number: ")
            pin = get_pin()
            product = input("What product(s) do you want to buy (e.g vegetables, beans): ")

            buyer = Buyer(name, phone_number, location, pin, product)
            buyer.registration()

        elif option == 3:
            # Go back to main menu
            continue
        else:
            print("Invalid option, please try again.")

    elif choice == 2:
        # Calling the function for user's login
        login_user()

    elif choice == 3:
        print("\nThanks for using Farm2Market. Goodbye!")
        break
