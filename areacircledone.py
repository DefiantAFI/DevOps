from math import pi
# import math


def area_of_circle(r):
    if r < 0:
        raise ValueError('Negative radius value error')
    value = pi*(r**2)
    # rounded = math.floor(value)
    return value


question = input('What\'s the radius of your circle in feet? ')
floatquestion = float(question)
floatquestion = area_of_circle(floatquestion)

while True:
    print(f'\nThe area of your circle is {floatquestion} feet')
