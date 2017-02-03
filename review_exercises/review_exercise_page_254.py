from random import randint

# Define rolls as as list
rolls = [0] * 6

for trial in range(0, 10000):
    die = randint(1, 6)
    # rolls[die - 1] finds the position on the list and += 1 statement adds one for it
    rolls[die - 1] += 1

print('1 = {}, 2 = {}, 3 = {}, 4 = {}. 5 = {}, 6 = {}'.format(*rolls))
