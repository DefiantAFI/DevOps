class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def getfull(self):
        full = f'Robot Name:                {self.name}\n'\
               f'Robot Color:               {self.color}\n'\
               f'Robot Weight:              {self.weight}'
        print('\n', type(full))
        return full


r1 = Robot("Cory", "red", 170)
r2 = Robot("zero", "black", 666)

print('\n', r1.getfull())
