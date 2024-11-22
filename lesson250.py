# a, b = 4, 5
# x, z = '4', '5'
#
# print(a + b)
# print(x + z)
# print(a.__add__(b))
# print(x.__add__(z))
# print(x.__add__('jjjjj'))
#
#

class Robot:
    """This class implements a Robot."""
    population = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Robot.population += 1

    def __del__(self):
        print(f'Robot {self.name} destroyed!')

    def __str__(self):
        my_str = f'My name is {self.name} and my price is {self.price}.'
        return my_str

    def __add__(self, other):
        price = self.price + other.price
        return price


r1 = Robot('Marvin', 150)
r2 = Robot('Gal', 45)

#print(r1 + r2)
#print(r1 > r2)
print(r1)
print(r1 + r2)







