from models.user import User
        
# Buyer's Method: Inherit Class User
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
        

