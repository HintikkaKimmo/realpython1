# Assignment page 121 translate.py for leekspeek

user_input = input('Please provide text to be translated to leekspeek: ')

print(str(user_input).replace('a', '4')\
    .replace('b', '8').replace('e', '3')\
    .replace('l', '1').replace('o', '0')\
    .replace('s', '5').replace('t', '7'))
