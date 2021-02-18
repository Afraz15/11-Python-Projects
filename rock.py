from random import randint

actions = ['rock', 'paper', 'scissor']

c_pic = actions[randint(0,2)]   # this will choose a number from 0-2 ( that number will call that index array)

player = input("Enter your action: ").lower() # This will convert the input text to lowercase   

if c_pic == player:
    print('Draw!!')
elif c_pic == 'rock' and player == 'paper':
    print('You win!!')
elif c_pic == 'rock' and player == 'scissor':
    print('You lose...')
elif c_pic == 'paper' and player == 'rock':
    print('You win!!')
elif c_pic == 'paper' and player == 'scissor':
    print('You win!!')
elif c_pic == 'scissor' and player == 'paper':
    print('You lose...')
elif c_pic == 'scissor' and player == 'rock':
    print('You lose...')



