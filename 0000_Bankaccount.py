# This is Mobile Money Aplication 
account = [[], []]


def line(txt):
    print('=' * len(txt))
    print(txt)
    print('='  * len(txt))
# Function to ask the User if wants to continue or making another transaction
#-----------------------------------------------------------------------------------------


def question():
    while True:
        ans = input('Do want to perfome another transaction? [Y/N]')
        if ans == 'n':
            break
        print("""Manage Your Account
        [1] Deposit
        [2] Withdrawal""")
        option = int(input('Select an option to perform a transaction! [1 or 2] ')) 
        if option == 1:
            account[1].append(float(input('Deposit your amount ')))
            for money1 in account[1]:
                addmoney = money + money1
            print(f'You deposited {money1} UGX to your account, Your Balance is {addmoney} UGX')
            print(f'Thanks to Use our Service!')
        
        elif option == 2:
            account[1].append(float(input('How Much Do u want to withdraw? UGX ')))
            for money2 in account[1]:
                addmoney = money - money2
            print(f'You removed {money2} UGX from your account, Your Balance is {addmoney} UGX')
            print(f'Thanks to Use our Service!')
#----------------------------------------------------------------------------------------------
line('WELCOME TO SANTOS BANK')
print(""" [1] Create Account""")
#try:
inp = int(input('Press 1 to Create account! '))
#except ValueError:
 #   print('Invalid details please enter Again')

if inp == 1:
    account[0].append(input('Enter your  full name! '))
    account[0].append(input('Enter your phone number! '))
    account[0].append(input('Enter your address '))
    account[0].append(input('Enter your Age! '))
    account[1].append(float(input('Enter the amout[UGX] 50.000 ')))
    # Here we created a loop to access the value inside account[1] the value in the account
    #====================================================================================
    for money in account[1]:
        if money < 50000:
            account[1].append(float(input('Amount is Less Than 50k Please Enter Other amount ')))
            print(f'Thanks! Account Created Successful')
    #========================================================================================
    #======================= Managing the account ===========================================
    print("""Manage Your Account
    [1] Deposit
    [2] Withdrawal""")
    option = int(input('Select an option to perform a transaction! [1 or 2] ')) 
    if option == 1:
        account[1].append(float(input('Deposit your amount ')))
        for money1 in account[1]:
            addmoney = money + money1
        print(f'You deposited {money1} UGX to your account, Your Balance is {addmoney} UGX')
        print(f'Thanks to Use our Service!')
        
    elif option == 2:
        account[1].append(float(input('How Much Do u want to withdraw? UGX ')))
        for money2 in account[1]:
            addmoney = money - money2
        print(f'You removed {money2} UGX from your account, Your Balance is {addmoney} UGX')
        print(f'Thanks to Use our Service!')
    # here we called the function to repeat the manage account process
    question()    
    # here we called the function to repeat the manage account process


