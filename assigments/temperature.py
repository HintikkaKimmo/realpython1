# Farenhight <> Celcius conversion formulas below
# F = C * 9/5 + 32
# C = (F - 32) * 5/9


def c_to_f(c):
    f = c * 9/5 + 32
    return '{} degrees C = {} degrees F'.format(c, f)


def f_to_c(f):
    c = (f - 32) * 5/9
    return '{} degrees F = {} degrees C'.format(f, c)

print(f_to_c(5))
print(c_to_f(5))

