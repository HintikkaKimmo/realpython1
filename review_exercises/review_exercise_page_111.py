weight = 0.2
animal = 'Newth'

print(str(weight) + ' kg is the weight of the ' + animal + '.')

print("{} kg is the weight of the {}.".format(weight, animal))

print("{0} kg is the weight of the {1}".format(weight, animal))

print("{weight} kg is the weight if the {animal}.".format(weight='0.2', animal='Newth'))
