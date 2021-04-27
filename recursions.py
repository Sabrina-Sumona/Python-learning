# Factorial of a number using loop
"""
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

print('Enter a number:')
num = input()


if int(num) < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif int(num) == 0:
    print("The factorial of 0 is 1")
else:
    fac = 1
    for i in range(1, int(num) + 1):
        fac = fac * i
    print("The factorial of "+str(num)+" is "+str(fac))
"""

# Factorial of a number using recursion
"""
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

print('Enter a number:')
num = input()

if int(num) < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif int(num) == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of "+str(num)+" is "+str(recur_factorial(int(num))))
"""

# sum 1 to n using loop
"""
print('Enter a number:')
n = input()

if int(n) < 0:
    print("Enter a positive number")
else:
    m = 0
    while int(n) > 0:
        m = m + int(n)
        n = int(n) - 1
    print("The sum = "+str(m))
"""

# sum 1 to n using recursion
"""
def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)

print('Enter a number:')
num = input()

if int(num) < 0:
    print("Enter a positive number")
else:
    print("The sum is "+str(recur_sum(int(num))))

"""

# reverse a list using loop
"""
def reverse_list(nums):
    new = []
    for i in range(0, len(nums)):
        new.append(0)
    for i in range(len(nums)-1, -1, -1):
        new[len(nums)-1-i] = nums[i]
    return new
my_list = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(my_list))
"""

# reverse a list using recursion
def rec_reverse_list(nums):
    if len(nums) == 0:
        return []
    return [nums[-1]]+rec_reverse_list(nums[:-1])

my_list = [1, 2, 3, 4, 5, 6, 7]
print(rec_reverse_list(my_list))

# find nth fibonacci using recursion
def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n-1) + rec_fib(n-2)

print(rec_fib(3))
