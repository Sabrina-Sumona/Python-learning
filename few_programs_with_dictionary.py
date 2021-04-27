# count frequency of char in a str
"""
import pprint as pp
# pprint is used to sort & print
text = 'this is sabrina sumona'
letters = {}
for i in text:
    letters.setdefault(i, 0)
    letters[i] = letters[i] + 1

pp.pprint(letters)
"""

# simulate a password protected app access
# """
passwords = {'Sumu': 9631, 'Nova': 1234, 'Tumpu': 1111}
matched = False
x = 0

print('Enter your name: ')

# here 5 attempt to enter name
while x < 3:
    name = input()
    if name in passwords:
        # here 5 attempt to enter password
        for i in range(0, 3):
            print('Enter your password: ')
            password = input()
            if int(password) == passwords[name]:
                matched = True
                print('Access granted')
                break
            else:
                print('Wrong password! Try again. You have '+str(2-i)+' chances left.')
    else:
        print('There is no such user! Try again. You have '+str(2-x)+' chances left.')
    x = x + 1
    if matched:
        break
# """

# make a phone book
"""
cont_no = {'Sumu': 123, 'Nova': 345, 'Tumpu': 567}
x = 0

while x < 5:
    print('Enter your name or press ENTER to exit: ')
    name = input()
    if name == '':
        break
    if name in cont_no:
        print('The contact number of '+name+' is '+str(cont_no[name]))
    else:
        print('The contact number of '+name+' is not found. Do you want to add?')
        ans = input()
        if ans == 'yes':
            print('Enter your number: ')
            num = input()
            cont_no[name] = num
            print('Number added successfully!')
        elif ans == 'no':
            print('Do you want to quit?')
            ans = input()
            if ans == 'yes':
                break
            elif ans == 'no':
                print('Keep searching')
        x = x + 1
"""
