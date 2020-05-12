import sys
studnt = []
while True:
    name = studnt.append(input('enter your name! '))
    age = studnt.append(int(input('how old are you? ')))
    gender = studnt.append(input('enter your gender [M/F]'))
    grade = studnt.append(float(input('enter your final grade')))
    rep = input('Do you want to continue? [Y/N] ')
    if rep == 'n':
        break
for pos, names in enumerate(studnt):
    print(f'the {pos} is {names}')
    if names == 3:
        print(f'{names}\n')














