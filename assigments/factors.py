# Assignment find the factor page 223

user_input = int(input('Enter a positive integer: '))

for n in range(1, user_input + 1):
    if user_input % n == 0:
        print('{} is divisor of {}'.format(n, user_input))




