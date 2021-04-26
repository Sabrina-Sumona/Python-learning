# Blocks are just groups of code, A block is marked by an equal amount of indentation.
# Indentations are just white-spaces at the beginning of the lines of python codes.

# Conditional Statements

# robot problem
"""
robot_move = input()

if robot_move == 'front':
    print('Moving Front')

elif robot_move == 'back':
    print('Moving Back')

else:
    print('Stand Still')

print('All done')
"""

# Loop

# while loop
"""
x = 0
while x <= 5:
    print(x)
    x = x+1
print('All done')
"""

# for loop

# range function
# range(start index,ending index + 1)
# range (3) : here loop will run 3 times (0,1 & 2) , by default staring is 0 and ending is (3-1 =) 2.
# range(0,4) : loop will run 0,1,2,3
# range(1,4): the loop will run like 1,2,3
# range (0, 10, 2) - will run from 0 to (10-1 =) 9 times and step size of the loop variable will increase by 2

"""
i = 0
for i in range(0, 3):
    print(i)
for i in range(1, 5):
    print(i)
for i in range(3):
    print(i)
for i in range(0, 10, 2):
    print(i)
for i in range(10, -1, -2):
    print(i)
for i in range(10, -4, -1):
    print(i)
"""

# infinite loop & break statement
"""
while True:
    print("Enter your name:")
    name = input()
    if name == "your name":
        break
print('Great job!')
"""

# continue statement
# Batman problem
"""
while True:
    print("Enter your name:")
    name = input()
    if name != "Batman":
        continue
    print('Hey '+name+'. What is the passcode?')
    passcode = input()
    if passcode == "Sabrina":
        break
print("Welcome to the Bat cave.")
"""

# sum of a series
"""
total = 0
for i in range(1, 5):
    total += i
print("Sum = "+str(total))
"""

# sum of a power series
"""
total = 0
for i in range(1, 5):
    total += i * i
print("Sum = "+str(total))
"""

# sum of a odd series
"""
total = 0
for i in range(1, 10, 2):
    total += i
print("Sum = "+str(total))
"""

# Nested loop
# sum of 1+(1+2)+(1+2+3)+(1+2+3+4) series
"""
total = 0
for i in range(1, 5):
    for j in range(1, i+1):
        total += j
print("Sum = "+str(total))
"""
