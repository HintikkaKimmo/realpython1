user_input = input('Please provide a word: ')

if len(user_input) < 5:
    print('{} is under 5 characters long!'.format(user_input))
elif len(user_input) == 5:
    print('{} is 5 characters long!'.format(user_input))
else:
    print('{} is over 5 characters long!'.format(user_input))
