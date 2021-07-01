def hello(**kwargs):
    for key, value in kwargs.items():
        print(type(kwargs))
        print("Hello", value, "!")


hello(kwarg1='Caleb', kwarg2='Sydney', kwarg3='Savannah')

input('stop :')
