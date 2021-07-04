class Robot:
    # Method functions must always use the self perameter
    def introduce_self(self):
        print("My name is " + self.name)


'''Creates the Robot object with three attributes'''
r1 = Robot()
r1.name = "Cory"
r1.color = "red"
r1.weight = 170

''' Runs the introduce_self member function and sends
r1 as the argument so r1.name = Cory'''
r1.introduce_self()

r2 = Robot()
r2.name = "zero"
r2.color = "black"
r2.weight = 666

r2.introduce_self()
print('\n', type(r1))
input('Hello: ')
