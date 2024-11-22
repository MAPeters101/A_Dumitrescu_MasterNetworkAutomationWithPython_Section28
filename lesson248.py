
class Robot:
    """This class implements a Robot."""
    def __init__(self, name, year):
        self.name = name
        self.year = year

r1 = Robot('R1', 2023)
print(r1.__doc__)
print(f'Robot name: {r1.name}')
print(r1.__dict__)



