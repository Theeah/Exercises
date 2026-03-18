from abc import ABC, abstractmethod

class Book:
    def __init__(self):
        self.__title: str
        self.__author: str
        self.__price: float

    def display_info(self):
        """Prints book info to the terminal."""
        print(f"{self.__title}, {self.__author}, {self.__price:.2f}")

    def get_price(self) -> float:
        return self.__price
    
    def set_price(self, new_price: float):
        if new_price>0:
            self.__price = new_price
        else:
            print("Price cannot be negative. Value was not updated.")
    
    def construct_book(self, title, author, price):
        """Makes a book with the information passed."""
        new_book = Book()
        new_book.__title = title
        new_book.__author = author
        new_book.set_price(price)
        return new_book

book1 = Book().construct_book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book1.display_info()

book2 = Book().construct_book("1984", "George Orwell", 8.99)
book2.display_info()

class BankAccount:
    def __init__(self):
        self.__account_number: str
        self.__balance = 0.00
    
    def deposit(self, amount: float):
        self.__balance = self.__balance + amount
    
    def withdraw(self, amount: float) -> bool:
        new_balance = self.__balance - amount
        if new_balance>0:
            self.__balance = new_balance
            return True
        else:
            print("Sorry, you do not have enough in your account.")
            return False
    
    def get_balance(self) -> float:
        return self.__balance
    
class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate: float
    
    def add_interest(self):
        added_interest = self.interest_rate * self.get_balance()
        self.deposit(added_interest)

save_account = SavingsAccount()
save_account.deposit(1000)
save_account.interest_rate = 0.1
save_account.add_interest()
print(save_account.get_balance())

class Device(ABC): #Defines an abstract class (one that should not be instanciated as is)
    def __init__(self):
        self.powered = False
        current_room: Room
    
    def toggle_power(self):
        """Toggle the power of the device.
        Sets powered to False if it is True and vice versa."""
        if self.powered == True:
            self.powered = False
        else:
            self.powered = True
    
    @abstractmethod
    def operate(self):
        pass

class Light(Device):
    def __init__(self):
        super().__init__()
        self.brightness = 0
    
    def operate(self):
        print(f"Brightness level: {self.brightness}")

class Thermostat(Device):
    def __init__(self):
        super().__init__()
        self.temperature = 24.0
    
    def operate(self):
        print(f"Temperature at {self.temperature} degrees.")

class Room():
    def __init__(self):
        self.name: str
        self.devices = []

class House():
    def __init__(self):
        self.rooms = []

    def master_switch(self):
        """Loops through all the devices in each room and turns them off."""
        for room in self.rooms:
            for device in room.devices:
                device.powered = False
                print("off")

h1 = House()
r1 = Room()
h1.rooms.append(r1)
bulb = Light()
themometer = Thermostat()
r1.devices.append(bulb)
r1.devices.append(themometer)

h1.master_switch()