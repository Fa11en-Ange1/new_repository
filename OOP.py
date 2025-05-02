#1.0. Create a Rectangle class to represent a rectangle.
#1.1. Add methods to calculate the area and perimeter of the rectangle.
#1.2. Create a Rectangle object and call these methods.


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


rect = Rectangle(7, 9)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())



# 2.0 Develop a BankAccount class to represent a bank account.
# 2.1 Add methods to withdraw and deposit funds to the account.
# 2.2 Use the magic __str__ method to display account information.

# class BankAccount:
#     def