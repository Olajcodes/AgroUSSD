from models.farmer import Farmer
from models.buyer import Buyer

def login_user():
    print("\n=== LOGIN MENU ===")
    print("1. Farmer Login")
    print("2. Buyer Login")
    print("3. Go Back")
    print("==================")

    while True:
        option = input("Enter choice (1/2/3): ")
        if option.isdigit() and int(option) in (1, 2, 3):
            option = int(option)
            break
        print("Enter a valid option (1/2/3)")

    if option == 1:
        phone = input("Enter your phone number: ").strip()
        pin = input("Enter your 4-digit PIN: ").strip()

        farmer = Farmer.find_by_phone(phone)
        if farmer and farmer.get("Pin") == pin:
            print(f"\nWelcome back, {farmer['Name']} (Farmer)!")
            #  Asking for option to update
            while True:
                print(f"\nWhat would you like to do?.")
                print("\n1. Update Profile")
                print("2. Exit")
                sub_option = input("Choose an option: ").strip()
                if sub_option == "1":
                    Farmer.update_profile(phone)  # call update method
                elif sub_option == "2":
                    print("Exiting Farmer menu...")
                    break
                else:
                    print("Invalid option, please try again.")
            return farmer
        else:
            print("Invalid phone number or PIN.")
            return None

    elif option == 2:
        phone = input("Enter your phone number: ").strip()
        pin = input("Enter your 4-digit PIN: ").strip()

        buyer = Buyer.find_by_phone(phone)
        if buyer and buyer.get("Pin") == pin:
            print(f"\nWelcome back, {buyer['Name']} (Buyer)!")
            #  Prompting for profile update
            while True:
                print(f"\nWhat would you like to do?.")
                print("\n1. Update Profile")
                print("2. Exit")
                sub_option = input("Choose an option: ").strip()
                if sub_option == "1":
                    Buyer.update_profile(phone)  # call update method
                elif sub_option == "2":
                    print("Exiting Buyer menu...")
                    break
                else:
                    print("Invalid option, please try again.")
            return buyer
        else:
            print("Invalid phone number or PIN.")
            return None

    elif option == 3:
        print("Going back to main menu...")
        return None