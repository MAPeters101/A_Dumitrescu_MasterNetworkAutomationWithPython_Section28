
class Robot:
    """This class implements a Robot."""
    population = 0
    def __init__(self, name, year):
        self.name = name
        self.year = year
        Robot.population += 1

    def __del__(self):
        print(f'Robot {self.name} destroyed!')

    def setEnergy(self, energy):
        self.energy = energy

r1 = Robot('R1', 2023)
r2 = Robot('Ben', 2040)
print(r1.__doc__)
print(f'Robot name: {r1.name}')
r1.setEnergy(500)
print(r1.energy)
#print(r1.brand)
print(r1.__dict__)
print(getattr(r1, 'energy'))
#print(getattr(r1, 'brand'))
print(getattr(r1, 'brand', 'N/A'))

print(f'Robots alive: {Robot.population}')











