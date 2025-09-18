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
        file_path = "/database/buyer.json"
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

            print(f"Buyer {self.name} registered successfully with PIN {self.pin}.")
            print("Make sure you keep your PIN safe.. Thank you")
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
        file_path = "/database/buyer.json"
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