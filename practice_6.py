# banking system
"""
accounts = {'Sumu': 500, 'Nova': 10000000000, 'Tumpu': 700000000}
print('Welcome to happy bank. Save today Happy tomorrow')

while True:
    print('Enter an option: ')
    print('1. View balance')
    print('2. View all info')
    print('3. Update balance')
    print('4. Exit')

    ans = input()

    if ans == '1':
        print('Enter your name: ')
        name = input()
        if name in accounts.keys():
            print('Hello '+name+'. Your balance is '+str(accounts[name]))
        else:
            print('The account of '+name+' is not found.  Do you want to add?')
            ans = input()
            if ans == 'yes':
                print(name+' please enter your balance: ')
                bal = input()
                accounts.update({name: bal})
                print('Account added successfully!')
            elif ans == 'no':
                print('Do you want to quit?')
                ans = input()
                if ans == 'yes':
                    break
                else:
                    print('Invalid option!')
            else:
                print('Invalid option!')
    elif ans == '2':
        for i, j in accounts.items():
            print("User name: "+str(i)+", Bank balance: "+str(j))
    elif ans == '3':
        print('Enter your name: ')
        name = input()
        if name in accounts.keys():
            print('Do you want to add or subtract?')
            ans = input()
            if ans == 'add':
                temp = accounts[name]
                print('How many amount do you want to add?')
                ans = input()
                accounts[name] = temp + int(ans)
                print('Balance successfully updated! Now your balance is '+str(accounts[name]))
            elif ans == 'add':
                temp = accounts[name]
                print('How many amount do you want to subtract?')
                ans = input()
                accounts[name] = temp - int(ans)
                print('Balance successfully updated! Now your balance is '+str(accounts[name]))
            else:
                print('Invalid option!')
        else:
            print('The account of '+name+' is not found.  Do you want to add?')
            ans = input()
            if ans == 'yes':
                print(name+' please enter your balance: ')
                bal = input()
                accounts.update({name: bal})
                print('Account added successfully!')
            elif ans == 'no':
                print('Do you want to quit?')
                ans = input()
                if ans == 'yes':
                    break
                else:
                    print('Invalid option!')
            else:
                print('Invalid option!')
    elif ans == '4':
        break
    else:
        print('Invalid option!')
"""

# print unique values
a = {1: 2, 2: 5, 5: 3, 4: 6, 3: 5, 7: 3, 9: 1}
b = {}
count = {}
for i in a.values():
    count.setdefault(i, 0)
    count[i] = count[i] + 1
i = 0
for k, v in count.items():
    if v == 1:
        b.update({i: k})
        i = i + 1
for i in b.values():
    print(i, end=" ")
