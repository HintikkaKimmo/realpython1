# Assignment page 165 track your investments


def invest(amount, rate, time):
    print('Principal amount ${}'.format(amount))
    print('annual rate of return: {}'.format(rate))
    print()
    for t in range(0, time + 1):
        amount = amount + (amount * rate)
        print('Year {}: ${}'.format(t, amount))
        print()

invest(100, 0.05, 8)
invest(2000, 0.25, 5)
