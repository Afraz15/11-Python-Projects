print('This program will give you your disocounted price')


def d_p(b):
    d_18 = 18 * b / 100
    f_18 = b - d_18
    d_20 = 20 * b / 100
    f_20 = b - d_20
    d_25 = 25 * b / 100
    f_25 = b - d_25
    arr = [f_18, f_20, f_25]
    c_d = input(f"To see discounts; Press 0 for 18%, 1 for 20% or 2 for 25%: ")
    c_ad = arr[int(c_d)]
    print(c_ad)
    d_p.arr = arr       # since everyting in python is an object so made this
    d_p.c_ad = c_ad


def e_p(ppl):
    e_p = d_p.c_ad / ppl    # 50-50
    print(e_p)


def ue_p(ppl):
    if ppl == 1:
        print(f'your total is: {d_p.c_ad}')
    elif ppl > 0 and ppl >= 2:
        p_70 = 70 * int(d_p.c_ad) / 100
        a_70 = d_p.c_ad - p_70
        r_p = a_70 / ppl
        print(f"One person can pay 70% : {p_70} and others can pay 30% : {r_p} ")

def sel(cout, ppl):
    if e_ue == '1':
        e_p(int(t_p))
    elif e_ue == '2':
        ue_p(int(t_p))

t_p = input('Enter your total price: ')
d_p(int(t_p))

t_p = input('Enter total number of people: ')

e_ue = input('press 1 to divide discount evenly or 2 for unevenly')

sel(e_ue, t_p)
