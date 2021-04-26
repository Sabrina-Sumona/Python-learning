# linear search

"""
def linear_search(my_list, item):
    for i in range(len(my_list)):
        if my_list[i] == item:
            return i
    return -1

a_list = [1, 7, 6, 5, 8]
print("Elements in the List :", a_list)
print("Now enter searching element :")
x = int(input())

result = linear_search(a_list, x)

if result == -1:
    print("Element " + str(x) + " is not found in the list")
else:
    print("Element " + str(x) + " is found at position " + str(result))

"""

# binary search

"""
# Returns index of x in arr if present, else -1

def binary_search(b_list, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if b_list[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left sub array
        elif b_list[mid] > x:
            return binary_search(b_list, low, mid - 1, x)

        # Else the element can only be present in right sub array
        else:
            return binary_search(b_list, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Test array
a_list = [2, 3, 4, 10, 40]
print("Elements in the List :", a_list)
print("Now enter searching element :")
y = int(input())

# Function call
result = binary_search(a_list, 0, len(a_list) - 1, y)

if result != -1:
    print("Element " + str(y) + " is found at position " + str(result))
else:
    print("Element " + str(y) + " is not found in the list")

"""

# create new odd list from a numbers list

"""
def odd_list(my_list):
    new_list = []
    k = 0
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            new_list.append(my_list[i])
    return new_list

a_list = [1, 7, 6, 5, 8, 2, 3, 4, 10, 40]

print("The list : ")
print(a_list)

result = odd_list(a_list)

print("The odd list : ")
print(result)

"""

# finding centered avg num from sorted/unsorted list

def centered_avg(my_list):
    sum = 0
    count = 0
    new_list = my_list.sort()
    for i in range(1, len(my_list)-1):
        sum = sum + my_list[i]
        count = count + 1
    return sum / count

a_list = [1, 7, 6, 5, 8, 2, 3, 4, 10, 40]

print("The list : ")
print(a_list)

result = centered_avg(a_list)

print("The centered average number of the list : ")
print(result)
