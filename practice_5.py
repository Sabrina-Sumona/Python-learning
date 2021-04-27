f = open('numbers', 'w+')
f.write('1234321')
f.close

f = open('numbers', 'r+')
my_list = list(f.read())
f.close()

is_palindromic = True

for i in range(int(len(my_list)/2)):
    if my_list[i] != my_list[len(my_list)-i-1]:
        is_palindromic = False

if is_palindromic:
    f = open('numbers', 'a')
    f.write('Yes')
    f.close()
else:
    f = open('numbers', 'w')
    for i in range(len(my_list)):
        f.write('0')
        f.close()
