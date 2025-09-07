from models.user import User

# Farmer's Method: Inherit Class User
class Farmer(User):
    def __init__(self, name, phone_number, location, pin, farm_size, primary_crop):
        super().__init__(name, phone_number, location, pin)
        self.farm_size = farm_size
        self.primary_crop = primary_crop
        
    def user_details(self):
        details = super().user_details()
        details.append({
            "Farm Size": self.farm_size,
            "Primary Crop": self.primary_crop
        })
        return details
