def hello(*args):
    for arg in args:
        for newarg in arg:
            print(newarg)

hello('Caleb', 'Sydney', 'Savannah')
