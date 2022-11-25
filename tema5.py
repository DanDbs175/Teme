from math import pi

# 1.
def addition(x, y):
    return x+y

print(addition(8, 12))
print(addition(7, -17))


# 2.
def par_impar(a):
    if a % 2 == 0:
        return True
    else:
        return False

print(par_impar(7))
print(par_impar(12))




# 4.
def arie_dreptunghi(L, l):
    print('Aria dreptunghiului este: ')
    return L*l

print(arie_dreptunghi(7, 5))
print(arie_dreptunghi(10, 4))


# 5.
def arie_cerc(raza):
    aria = pi * raza**2
    return aria

print(arie_cerc(5))
print(arie_cerc(7))

# 6.


def find_char(x, given_str):
    if x.lower() in given_str:
        return True
    else:
        return False

print(find_char('.', 'Nu stiu ce string sa scriu aici.'))
print(find_char('U', 'Nu stiu ce string sa scriu aici.'))
print(find_char('M', 'Nu stiu ce string sa scriu aici.'))


# 7.
def lower_upper_count(str):
    c1 = 0
    c2 = 0 # tine de cate ori un caracter e lowercase
    for i in range(len(str)):
        if str[i] == ' ':
            continue
        if str[i].isupper():
            c1 +=1
        else:
            c2 +=1
    print(f'Nr de caractere upper case este {c1}.')
    print(f'Nr de caractere lower case este {c2}.')

print(len('CERUL are niste culori splendide IN ACEASTA seara.'.replace(' ', '')))
lower_upper_count('CERUL are niste culori splendide IN ACEASTA seara.')
lower_upper_count('CERUL ARE niste culori splendide in aceasta seara.')


# 8.
def positive_ones(lst):
    lst_pos = []
    for i in lst:
        if i > 0:
            lst_pos.append(i)
    return lst_pos

print(positive_ones([1, 5, -8, 12, -6]))
print(positive_ones([-9, 7, 5, -3, 1]))


# 9.
def compare(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}.')
    elif x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}.')
    else:
        print('Numerele sunt egale.')

compare(5, 9)
compare(7, -2)
compare(8, 8)

