print('This program Collects the Uppercase letter and make a single word out of them \n')

n = input("Enter text: ")
a = []
h = list(n)

for i in h:
    if i.isupper():
        a.append(i)
b = "".join(a)
print(b)


