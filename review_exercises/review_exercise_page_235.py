

while True:
    user_input = input('Provide input or q / Q to quit: ')
    if str(user_input).lower() == 'q':
        break

for i in range(0, 50 + 1):
    if i % 3 == 0:
        continue
    print(i)
