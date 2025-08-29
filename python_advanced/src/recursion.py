#1
def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


#3
def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


#5
class CamelCase(type):
    def __new__(cls, name, bases, namespace):
        if not name[0].isupper():
            raise TypeError("Class name not in CamelCase")
        return super().__new__(cls, name, bases, namespace)


class MyClass(metaclass=CamelCase):
    pass


class notCamelCase(metaclass=CamelCase):
    pass
