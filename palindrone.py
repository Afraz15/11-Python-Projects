print('This program is used to check if your entered word is palindrome or not')

word = input('Enter a 5 letter word')

app = ''.join(reversed(word))

print(app)

if word == app:
    print('your entered word is palindrome!')
else:
    print('your entered word is not palindrome...')
