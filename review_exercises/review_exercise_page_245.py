while True:
    try:
        user_input = input('Please provide an integer: ')
        user_input = int(user_input)
        break
    except ValueError:
        print('Not an integer! Please try again.')
print('Great you managed to provide a real integer {}'.format(user_input))
