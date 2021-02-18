from random import randint

c_num = randint(0, 50)

i = 0
tries = 0

while i == 0:
    u_num = int(input('Enter your number: '))
    tries = tries + 1

    if u_num > 50:
        u_num = input('Enter number from 0-50: ')

    if u_num == c_num:
        print('\n You got the right answer!!!')
        print(f'Number of tries were {tries}')
        i = 1
    else:
        print('your answer was wrong')
