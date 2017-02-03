from random import randint

flips = 0

for tries in range(0, 10000):
    flip = randint(0, 1)
    flips += 1
    while flip != randint(0, 1):
        flips += 1

print(flips)
print('On average you need {} to get 2 of the same'.format((flips / 10000)))

# TODO this is giving avarage of 2 needed flips which is wrong need to check the logic
