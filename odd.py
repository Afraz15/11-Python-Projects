print("Welcome to the program to check your number ( if it's odd or even )")


def check(num):
    a = num % 2
    if a == 1:
        print(f"The number is odd ( number = {num} )")
    elif a == 0:
        print(f"The number is even ( number = {num} )")


# num = input("Enter your number: ")
num = int(input("Enter number to check"))

check(num)
