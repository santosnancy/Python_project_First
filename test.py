account = []
def line(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))


while True:
    line('welcome to login application'.upper())
    file = open('C:\\Users\\diplo\\Documents\\Python_project_First\\login.txt', 'a+')
    name = account.append(file.write(input('Enter your username!')))
    password = account.append(file.write(input('Enter  the password for your account!')))
    question = input('Press [Y] to continue! and [N] to stop! ')
    if question == 'n':
        break
    else:
        continue





