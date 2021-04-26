# Leap year problem
"""
year = int(input("Enter a year:"))
if year % 400 == 0:
    print(str(year)+" is a leap year.")
elif year % 100 == 0:
    print(str(year)+" is not a leap year.")
elif year % 4 == 0:
    print(str(year)+" is a leap year.")
else:
    print(str(year)+" is not a leap year.")
"""
# pattern 1
"""
row = int(input("Enter the no. of rows:"))
count = 0
for i in range(0, row):
    for j in range(0, row-i-1):
        # end defines the ending of print function
        print(end=" ")
    count = count + 1
    for k in range(0, i+count):
        print("*", end="")
    # default ending of print is new line
    print()
"""

# pattern 2
row = int(input("Enter the no. of rows:"))
for i in range(0, row):
    for j in range(0, row-i-1):
        # end defines the ending of print function
        print(end=" ")
    for k in range(0, i+1):
        print("*", end="")
    # default ending of print is new line
    print()

# Armstrong no.
"""
n = int(input("Enter a 3 digit no.:"))
a = int(n / 100)
b = int((n % 100) / 10)
c = n % 10
d = a ** 3 + b ** 3 + c ** 3
if n == d:
    print(str(n)+" is an armstrong no.")
else:
    print(str(n)+" is not an armstrong no.")
"""
