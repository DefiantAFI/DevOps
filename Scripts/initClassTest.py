class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def getfull(self):
        full = f' {self.name} '
        print('\n', type(self.name))
        return full


r1 = Robot("Cory", "red", "170")
r2 = Robot("zero", "black", "666")

print('\n', r1.getfull())
a = {'set': 'shoes'}
print('\n', type(a))
