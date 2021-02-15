print('This program will give your entered data')

def n_check(info):
    if len(info) < 3:
        name = input('Enter valid information')
    else:
        print(info)

def d_check(info):
    if info > 31 and info > 0:
        print(info)
        day = input('your date must be between 1-31: ')

def y_check(info):
    if info > 2021:
        year = input('Enter your date of birth correctly: ')    # don't go in the future just yet

name = input("Enter your name: ")
n_check(name)

ar = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
m_num = input('Enter a number from 0-11 to select month ( Jan-Dec ):')
mon = ar[int(m_num)]
day = input('Enter your date: ')
d_check(int(day))
year = input('Enter your Year: ')
y_check(int(year))

adr = input('Enter your address: ')
prof = input('Enter your dream/profession: ')

print(f"Hello {name} \n According to your info \n\n Your Date of birth is: {mon} {day} , {year} \n Your address is: {adr} \n And your Dream/Profession is {prof}. \n")





