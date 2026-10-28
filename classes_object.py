## classes with instance variables
'''
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1=Dog("puppy",5)
print("Dog name is:",dog1.name, "\nDog age is:",dog1.age)

## classes with  instance methods
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} says woof!")
dog1 = dog("puppy",5)
dog1.bark()

'''
## Bank Management System

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposit of {amount} made. New balance is: {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print(f"Withdrawal of {amount} made. New balance is: {self.balance}")
    def get_balance(self):
        return self.balance
b1=BankAccount("sms",5000)
b1.deposit(1000)
b1.withdraw(2000)
print("Current balance is:",b1.get_balance())
