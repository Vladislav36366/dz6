my_dict = {'Vlad' : 2004 , 'Danya': 2005 }
print(my_dict)
print(my_dict['Vlad'])
print(my_dict.get('Dima','Такого ключа нет'))
my_dict.update({'Nikita' : 2002,
                'Ilya' :2003 })
a = my_dict.pop('Danya')
print(a)
print(my_dict)

my_set = {1, 1, 'Яблоко', 42.5, 42.5}
print(my_set)
my_set.add(43)
my_set.add((9, 5, 4.9))
my_set.remove(1)
print(my_set)

