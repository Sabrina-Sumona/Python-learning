# odd or even
"""
def check_even_odd(n):
    if n % 2 == 0:
        print('This is an even number')
    else:
        print('This is an odd number')

print('Enter a number:')
a = int(input())

check_even_odd(a)
"""

# prime no
"""
import math

def check_prime(n):
    count = 0
    if n == 1:
        print('This is not a prime number')
    else:
        # this math formula is used to optimize the solution
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                print('This is not a prime number')
                break
            count = count + 1
        if count+2 == math.floor(math.sqrt(n))+1:
            print('This is a prime number')

print('Enter a number:')
a = int(input())

check_prime(a)
"""

# Area of circle, rectangle, square, triangle, trapezium
"""
def area_func():
    print('Enter the shape to find the area: ')
    shape = input()

    if shape == 'CIRCLE':
        print('PLEASE ENTER THE RADIUS: ')
        r = float(input())
        area = 3.1416 * r * r
        print('The area is: ')
        print(area)

    elif shape == 'TRIANGLE':
        print('PLEASE ENTER THE BASE: ')
        base = float(input())
        print('PLEASE ENTER THE HEIGHT: ')
        height = float(input())
        area = 0.5 * base * height
        print('The area is: ')
        print(area)

    elif shape == 'RECTANGLE':
        print('PLEASE ENTER THE LENGTH: ')
        length = float(input())
        print('PLEASE ENTER THE WIDTH: ')
        width = float(input())
        area = length * width
        print('The area is: ')
        print(area)

    elif shape == 'SQUARE':
        print('PLEASE ENTER THE LENGTH: ')
        length = float(input())
        area = length * length
        print('The area is: ')
        print(area)

    elif shape == 'TRAPEZIUM ':
        print('PLEASE ENTER THE SIDE 1: ')
        side1 = float(input())
        print('PLEASE ENTER THE SIDE 2: ')
        side2 = float(input())
        print('PLEASE ENTER THE HEIGHT: ')
        height = float(input())
        area = 0.5 * (side1 + side2) * height
        print('The area is: ')
        print(area)

    elif shape == 'RHOMBUS':
        print('PLEASE ENTER THE DIAGONAL 1: ')
        diagonal1 = float(input())
        print('PLEASE ENTER THE DIAGONAL 2: ')
        diagonal2 = float(input())
        area = 0.5 * diagonal1 * diagonal2
        print('The area is: ')
        print(area)

area_func()
"""

# HCF(Highest Common Factor) between 2 no.
"""
def hcf_func(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    ans = 0
    print('The common factors between '+str(a)+' and '+str(b)+' :')
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            ans = i
            print(ans)
    return ans

print('Enter the numbers:')
x = int(input())
y = int(input())
z = hcf_func(x, y)
print('The highest common factor is : '+str(z))
"""

# Rock-paper-scissors game

print('For player1: what do yo want to choose? rock, paper or scissors?')
p1 = input()

print('For player1: what do yo want to choose? rock, paper or scissors?')
p2 = input()

def game(a, b):
    if a == b:
        return "It's a tie!"
    elif a == 'rock':
        if b == 'scissors':
            return "Rock beats scissors!"
        else:
            return "Paper beats rock!"
    elif a == 'scissors':
        if b == 'paper':
            return "Scissors beat paper!"
        else:
            return "Rock beats scissors!"

    elif a == 'paper':
        if b == 'rock':
            return "Paper beats rock!"
        else:
            return "Scissors beat paper!"

    else:
        return "Wrong input. Please enter rock, paper or scissors."

print(game(p1, p2))
