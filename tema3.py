# 1.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
lista_inversata = note_muzicale[::-1]
print(lista_inversata)
lista_inversata.reverse()
print('Dupa inversarea inversarii lista este: ', lista_inversata)

#2.
print('"do" apare de ', note_muzicale.count('do'), ' ori."')

#3.
list1 = [3, 1 , 0, 2]
list2 = [6, 5, 4]
lst_merged = list1 + list2
print(lst_merged)

list1.extend(list2)
print(list1)

#4.
lst_sorted = sorted(list1)
print(lst_sorted)

#5.
if len(lst_merged) == 0:           # sau empty = [] si comparare cu lista mea
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

# 6/7.
lst_merged.clear()
if len(lst_merged) == 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

#8.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())
#9.
print('Ana a luat nota ',dict1.get('Ana'),'.', sep='')
print('Gigel a luat nota ',dict1.get('Gigel'),'.', sep='' )
print('Dorel a luat nota ', dict1.get('Dorel'),'.', sep='')

#10.
dict1['Dorel'] = 6
print('Dupa marire, nota lui Dorel este', dict1.get('Dorel'))

#11
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1.keys())


