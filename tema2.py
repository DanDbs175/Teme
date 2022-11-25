#1
#If else reprezinta doua moduri conditionale de lucru
#2
x = int(input('x='))
if x >= 0 :
    print('Numarul este natural')
else :
    print('Numarul nu este natural')

#3
x1 = int(input('x1='))
if x1==0:
    print('Numarul este neutru')
elif   x1 < 0:
   print('Numarul este negativ')
else:
     print('Numarul este pozitiv')
#4
x2 = int(input('x2='))
if x2>=-2 and x2<=13:
    print('Apartine sirului')
else:
    print('Nu apartine sirului')
#5
x3=int(input('x3='))
y3=int(input('y3='))
if (x3-y3)<5:
    print('Diferenta este mai mica decat 5')
else:
    print('Diferenta este mai mare decat 5')

#6
x4=int(input('x4='))
if  not (x4>=5 and x4<=27):
    print(f'Nu se afla in sir')
else:
    print(f'Se afla in sir')

#7
x5=int(input('x5='))
y5=int(input('y5='))
if x5==y5:
    print('Felicitari..numerele sunt egale')
elif x5>y5:
    print('x5 mai mare ca y5')
else:
    x5<y5
    print('y5 mai mare ca x5')

#8
x6=int(input('x6='))
y6=int(input('y6='))
z6=int(input('z6='))
if x6!=y6!=x6 :
    print('Triunghiul este oarecare')

elif  x6==y6!=z6   or  y6==z6!=x6  or   x6==z6!=y6 :
    print('Triunghiul este isoscel')

else:
      x6==y6==z6
      print('Triunghiul esti echilateral')

#9
x7 = str(input('x7='))
if x7 in 'aeiou' :
       print(f'Litera este vocala')
else:
    print('Litera este consoana')






