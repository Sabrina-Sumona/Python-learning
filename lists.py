"""
# making a list
# its look like array but more flexible than array

# num list
a = [1, 2, 3, 4, 5, 6]

# str list
b = ['a', 'b', 'c']

# mixed list
c = [1, 5.2, 3, 'a', 'aab', 'c']

print(a)
print(b)
print(c)

# individual element of the list print
print(c[3])

# nested list
# outer list & inner list
x = [[11, 12, 13], ['ab', 'bc', 'cd']]
# combine nested list
y = [[a], [b]]

print(x)
print(y)

# individual element of the nested list print
print(x[1][2])
print(x[0][0])

# negative indexes
# -1 means last element
print(c[-1])
# -2 means 2nd last element
print(c[-2])

# sub lists & slicing
# starts from index 0 & ends index before 5
print(a[0:5])
# starts from index 2 & ends index before 4
print(a[2:4])

# slice using negative index
# starts from index 0 & ends index before 3rdd last
print(a[0:-3])
# starts from index 1 & ends index before 2nd last
print(a[1:-2])
# starts from index 4th last & ends index before 1st last
print(a[-4:-1])

# if start does not given by default starts from 0 index
print(a[:6])

# if ends does not given by default ends at last index
print(a[0:])

# if start  & ends does not given by default starts from 0 index & ends at last index
print(a[:])

"""

# modify a list

# combine
a =[1, 2, 3]
b = [4, 5, 6]
ab = a + b
print(ab)

# make double elements
x = ['p', 'q', 'r']
y = x * 2
print(y)

# delete element
del ab[2]
print(ab)

