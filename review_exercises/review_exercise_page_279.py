desserts = ['ice cream', 'cookies']

desserts.sort()
print(desserts)
print(desserts.index('ice cream'))
foods = desserts[:]
foods.extend(['broccoli', 'turnips'])
print(desserts, foods)
foods.remove('cookies')
print(foods[0:2])
breakfast = 'cookies, cookies, cookies'.split(',')
print(breakfast)

# num_list = [2, 4, 8, 16, 32, 64]

# print(num_list)


def from_1_to_20(l):
    # Python list comprehension explained at > http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
    return print([x for x in l if x <= 20])

from_1_to_20([2, 4, 8, 16, 32, 64])


# TODO figure why print(desserts.sort()) returns None
