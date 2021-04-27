# find number of digits using recursion
def digit(x):
    if x == 0:
        return 0
    return 1 + digit(x // 10)

print(digit(1025550))

# int exponentiation
def exponent(x, y):
    if y == 0:
        return 1
    else:
        return x * exponent(x, y-1)

print(exponent(2, 5))
