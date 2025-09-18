from models.user import User
import os
import json

# Farmer's Method: Inherit Class User
class Farmer(User):
    def __init__(self, name, phone_number, location, pin, farm_size, primary_crop):
        super().__init__(name, phone_number, location, pin)
        self.farm_size = farm_size
        self.primary_crop = primary_crop
        
    def user_details(self):
        details = super().user_details()
        details.update({
            "Farm Size": self.farm_size,
            "Primary Crop": self.primary_crop
        })
        return details
    
    def registration(self):
        file_path = "/database/farmer.json"
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
                if any(farmer.get("Phone Number") == self.phone_number for farmer in data):
                    print(f"Farmer with phone {self.phone_number} already exists.")
                    return True

                new_farmer = self.user_details()
                data.append(new_farmer)
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

            print(f"Farmer {self.name} registered successfully with PIN {self.pin}.")
            print("Make sure you keep your PIN safe.. Thank you")
            return False
        
        except FileNotFoundError:
            #create empty file if file doesn't exist
            with open(file_path, "w") as file:
                json.dump([],file)
            #then do the Registration again
            self.registration()
            
        except json.JSONDecodeError as e:
            print(f"Farmer.json contain invalid JSON: {e}")
            return True
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            return True
        
        
    @staticmethod
    def find_by_phone(phone_number):
        """
        Look up a farmer by phone number.
        Returns dict if found, else None.
        """
        file_path = os.path.join(os.path.dirname(__file__), "..", "database", "farmer.json")
        if not os.path.exists(file_path):
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for farmer in data:
                    if farmer.get("Phone Number") == phone_number:
                        return farmer
        except (json.JSONDecodeError, FileNotFoundError):
            return None
        return None