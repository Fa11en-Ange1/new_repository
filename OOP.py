#1.0. Create a Rectangle class to represent a rectangle.
#1.1. Add methods to calculate the area and perimeter of the rectangle.
#1.2. Create a Rectangle object and call these methods.


# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return 2 * (self.a + self.b)
#
#
# rect = Rectangle(7, 9)
# print("Area:", rect.area())
# print("Perimeter:", rect.perimeter())



# 2.0 Develop a BankAccount class to represent a bank account.
# 2.1 Add methods to withdraw and deposit funds to the account.
# 2.2 Use the magic __str__ method to display account information.

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited: {amount} units')
        else:
            print('Deposit amount must be greater than 0')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        elif amount <= 0:
            print('Withdrawal amount must be greater than 0')
        else:
            self.balance -= amount
            print(f'Withdrawn: {amount} units')

    def __str__(self):
        return f'Account Owner: {self.owner}, Balance: {self.balance:.2f} units'
