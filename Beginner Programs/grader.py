while True:
    try:
        grade = int(input('Input your grade as a number: '))

    except ValueError:
        print('\nYour input is not a valid integer')

    else:
        if grade >= 0 and grade <= 100:
            break

        else:
            print('Not in the A-F Range!\n')

    # finally:

if grade >= 90:
    print('\nContrats you got an A!!')

if grade >= 80 and grade <= 89:
    print('\nNice job on the B!')

if grade >= 70 and grade <= 79:
    print('\nClass a little tough?')

if grade >= 60 and grade <= 69:
    print('\nOMG what happened?')

if grade >= 0 and grade <= 59:
    print('\nYou\'re a failure!')

input('Press Enter to Exit')
