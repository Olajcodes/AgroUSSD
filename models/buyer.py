from models.user import User
import os
import json

class Buyer(User):
    def __init__(self, name, phone_number, location, pin, product):
        super().__init__(name, phone_number, location, pin)
        self.product = product

    def user_details(self):
        details = super().user_details()
        details.update({
            "Product": self.product
        })
        return details

    def registration(self):
        file_path = r"database\buyer.json"
        # Make sure file exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        try:
            if not os.path.exists(file_path):
                with open(file_path, "w") as file:
                    json.dump([], file)

            with open(file_path, "r+", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []

                # check if user with same phone number exists
                if any(buyer.get("Phone Number") == self.phone_number for buyer in data):
                    print(f"Buyer with phone {self.phone_number} already exists.")
                    return True

                new_buyer = self.user_details()
                data.append(new_buyer)

                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

            print(f"Congratulations! Buyer {self.name} registered successfully\nBelow is your pin: {self.pin}.")
            print("Please ensure not to share your pin with anyone. Thank you")
            return False

        except FileNotFoundError:
            with open(file_path, "w") as file:
                json.dump([], file)
            self.registration()

        except json.JSONDecodeError as e:
            print(f"buyer.json contains invalid JSON: {e}")
            return True

        except Exception as e:
            print(f"Unexpected error: {e}")
            return True

    @staticmethod
    def find_by_phone(phone_number):
        """
        Look up a buyer by phone number.
        Returns dict if found, else None.
        """
        file_path = r"database\buyer.json"
        if not os.path.exists(file_path):
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for buyer in data:
                    if buyer.get("Phone Number") == phone_number:
                        return buyer
        except (json.JSONDecodeError, FileNotFoundError):
            return None
        return None
    
    
    # For profile management
    @staticmethod
    def update_profile(phone_number):
        file_path = r"database\buyer.json"
        if not os.path.exists(file_path):
            print("No buyer database found.")
            return

        with open(file_path, "r+", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("Database corrupted.")
                return

            buyer = next((b for b in data if b.get("Phone Number") == phone_number), None)
            if not buyer:
                print("Buyer not found.")
                return

            print("\n=== PROFILE MANAGEMENT (Buyer) ===")
            print("1. Update Name")
            print("2. Update Location")
            print("3. Update Phone Number")
            print("4. Change PIN")
            print("5. Update Product")
            print("0. Exit")

            choice = input("Select an option: ").strip()
            if choice == "1":
                buyer["Name"] = input("Enter new name: ").strip().title()
            elif choice == "2":
                buyer["Location"] = input("Enter new location: ").strip().title()
            elif choice == "3":
                buyer["Phone Number"] = input("Enter new phone number: ").strip()
            elif choice == "4":
                new_pin = input("Enter new 4-digit PIN: ").strip()
                if new_pin.isdigit() and len(new_pin) == 4:
                    buyer["Pin"] = new_pin
                else:
                    print("Invalid PIN. Must be 4 digits.")
            elif choice == "5":
                buyer["Product"] = input("Enter new product: ").strip()
            elif choice == "0":
                print("Exiting profile management...")
                return
            else:
                print("Invalid option.")
                return

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            print("Profile updated successfully.")