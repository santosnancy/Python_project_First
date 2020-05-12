account = [[], []]
# this function will display the name of the txt input
# within equal quotations
def line(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))


line('welcome to uba bugema'.upper())
print("""\033[1;34mChoose any option bellow to manane your account!
1 - open account
2 - deposit
3 - withdrawal
4 - close the application\033[m""")
option = int(input('\033[1;31mchoose any option [1 up to 4]\033[m'))
# here we have a number of option to choose from
# 1 - will append all the input at account[0] the first list inside the
# main account list
if option == 1:
    name = account[0].append(input('enter your name! '))
    address = account[0].append(input('Enter your address '))
    dob = account[0].append(int(input('enter your date of birth ')))
    openbal = account[1].append(float(input('Enter the open balance UGX [100000]')))
    # here we created a loop to allow only deposit greater than 100
    for balance in account[1]:
        if balance < 100000:
            openbal = account[1].append(float(input('the amount is less at least 100.000 UGX ')))
        else:
            print('\033[1;31mCongratulation to open the account at UBA BUGEMA BRANCH\033[m')
    for lopes in account[0]:
        print(f' Hello {lopes}', end=' ')
    for car in account[1]:
        print(f' your have {car} USD in your Account')

