# This is my 1st code in python

# string can be written with "..." or '...'
print("Hello!!")
# print is output function
print('This is Sabrina.')

# python doesn't require data type declaration
# python always clear the memory that  variable holds after use
# integer division
a = 5//2
print(a)

# exponentiation
# power
b = a**3
print(b)

# syntax error
# c = 9+
# 7

# operators with string
c = 'python '*2
print(c)
d = 'python '+'is '+'awesome '
print(d)

# int with float
e = 2 + 7.5
print(e)
# string with int/float shows error
# f = 'abc'+123

# variable overriding
a = 44
print(a)

# True/False boolean data types are case sensitive
# python can't concatenate string & int/float
# binary boolean : and , or, not etc. ( not as c, c++)

# # input is input function
# a = input()
# # input function always take inputs as string
# print(a)
#
# # type testing
# t = type(a)
# print(t)

# type casting
# float to int
print(int(98.7))
# int to float
print(float(98))
# int/float to string
print(str(98.7))
t = type(str(98.7))
print(t)

# length of string
print(len(str(98.7)))
print(len(str('Sumona')))

# a simple problem
print('Hello! What is your name?')
name = input()
print('How old are you ' + name)
age = input()
birth_year = 2021-int(age)
ans = str(birth_year)
print('So, you are born in ' + ans)
