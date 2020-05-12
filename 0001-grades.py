students = []
# here we created a function  text message to display when the program starts
def prlogin(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))



prlogin('welcome to grade system'.upper())
nmb = int(input('Enter the number the students! '))
best = 100
for n in range(0, nmb): # loop to count how many grade we are going to insert
    grd = students.append(int(input(f'enter the graade of the first {n + 1}o students ')))
print('=' * 20)
for pos, std in enumerate(students):
    print(f'students {pos + 1}o scored {std}')

for aveg in students: # loop to calculate the average by assigning letters
    if aveg >= best - 10:
        print(f' You got A')
    elif aveg >= best - 20:
        print(f'You got B')
    elif aveg >= best - 30:
        print(f'You got C')
    elif aveg >= best - 40:
        print(f'You got D')
    else:
        print(f'Bad luck you have failed')
        


