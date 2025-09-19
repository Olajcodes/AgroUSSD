## **USSD Digital Marketplace**
A Python-based USSD-like digital marketplace simulation where Farmers and Buyers can register, log in, and manage their profiles.
Data is stored in lightweight JSON files (database/farmer.json, database/buyer.json) for persistence.

### **Features**
1. Farmer Registration and Login
- Store farm size and primary crop details
- Profile update support

2. Buyer Registration & Login

- Save product of interest

- Profile update support

3. Secure Login using phone number + 4-digit PIN

4. JSON Database

- Farmers: database/farmer.json

- Buyers: database/buyer.json

5. USSD-like Console Menus

- Main menu

- Registration menu

- Login & profile management


### **Project Structure**
```
├── main.py                # Entry point (menus & navigation)
├── models/
│   ├── user.py            # Base User class
│   ├── farmer.py          # Farmer model & methods
│   ├── buyer.py           # Buyer model & methods
├── database/
│   ├── farmer.json        # Farmer data storage
│   ├── buyer.json         # Buyer data storage
└── README.md              # Project documentation
```
