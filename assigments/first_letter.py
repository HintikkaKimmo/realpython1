# Assignment page 95 Real Python part 1

user_input = str(input('Tell me your password: '))
if user_input != '':
    print('Your passwords first letter in UPPERCASE is', user_input[0].upper())
else:
    print('You need to answer something!')
