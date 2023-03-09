"""Use a função map() para aplicar uma função em cada elemento de uma lista"""
print('--------------map-----------------\n')
# usando loop
my_list = [1, 2, 3, 4, 5]
new_list = []
for element in my_list:
    new_list.append(element**2)
print(new_list)

# usando map
my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x**2, my_list))
print(new_list)

print('\n--------------zip------------------\n')

"""Use a função zip para iterar em multiplas listas em paralelo"""

# usando loop
list1 = [1, 2, 3]
list2 = ["a","b","c"]
for i in range(len(list1)):
    for j in range(len(list2)):
        if i == j:
            print(list1[i], list2[j])

# usando a função zip 
list1 = [1, 2, 3]
list2 = ["a","b","c"]
for item1, item2 in zip(list1, list2):
    print(item1, item2)

"""Slicing para malipular listas
- Extrair 
- Manipular
- Criar novas listas a partir de outra existente
"""

print('\n--------------slicing------------------\n')

# usando loop
my_list = [1, 2, 3, 4, 5]
new_list = []
for i in range(1, len(my_list) -1):
    new_list.append(my_list[i])
print(new_list)

# usando slicing
my_list = [1, 2, 3, 4, 5]
new_list = my_list[1: -1]
print(new_list)