"""def f1():
    print('Hello')


f1()


def add(a, b):
    return a + b


ans = add(5, 2)
print(ans)


def print_name(name):
    print('Welcome to Python learning ' + name)

my_name = input('Enter your name:')
print_name(my_name)"""

# print function is a NoneType function
"""
print(type(print()))
"""

# keyword argument - end

# default ending of print is new line
# end defines the ending of print function
"""
print('Hello ', end='')
print('World')
"""

# keyword argument - sep

# default separation of print is space
# sep defines the separation of print function
"""
print('a', 'b', 'c', sep=',')
"""

# scopes - global & local scope
"""
a = 5
b = 3


def f():
    c = 10
    global b
    print(c)
    # not shows error as a is global variable
    print(a)
    # not shows error as b is declared as global variable
    print(b)


"""
# shows error as c is local variable
# print(c)
"""
f()
"""

# if a variable print before initialization it shows error

# Exception handling
"""
def exe_hn(x):
    try:
        return 100 / x
    except:
        return 'There is a zero division error'


answer = exe_hn(0)
print(answer)
"""

# Fibonacci sequence
# 0 1 1 2 3 5 8 13

"""
def fibonacci(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        print(x)
        print(y)

        for i in range(1, n):
            z = x+y
            x = y
            y = z
            print(z)


fibonacci(7)
"""

# Guess my age game

import random as r

secret_age = r.randint(1, 10)
flag = False

print('Guess the age between 1 to 10: (You have total 3 guesses)')
print(str(secret_age))

def game_func(guessed_age, secret):
    if guessed_age < secret:
        return 'Too low'
    elif guessed_age > secret:
        return 'Too high'
    else:
        return 'Correct!'


for i in range(1, 4):
    guess = input()
    if game_func(int(guess), secret_age) == 'Correct!':
        print('You won the game!')
        flag = True
        break
    elif game_func(int(guess), secret_age) == 'Too high':
        print('Enter a small number.')
        flag = False
    elif game_func(int(guess), secret_age) == 'Too low':
        print('Enter a large number.')
        flag = False
    print('You have ' + str(3 - i) + ' guesses left.')

if not flag:
    print('You lost the game. Correct age is ' + str(secret_age))
