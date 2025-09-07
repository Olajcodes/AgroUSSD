
class User:
    def __init__(self, name, phone_number, location, pin = 0000):
        self.name = name
        self.phone_number = phone_number
        self.location = location
        self.pin = pin
        
    # To get user details
    def user_details(self):
        return {
            "Name":self.name,
            "Phone Number": self.phone_number,
            "Location": self.location,
            "Pin": self.pin
        }