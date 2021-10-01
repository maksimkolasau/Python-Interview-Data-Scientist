import copy

# link to original
list1 = [['a'], ['b'], ['victor'], ['d'], ['roma'], ['pavel'], ['4']]
list2 = list1
list1[2] = ['original changes']
print(list2)
print('')

# shallow copy
list1 = [['a'], ['b'], ['victor'], ['d'], ['roma'], ['pavel'], ['4']]

list3 = copy.copy(list1)
list1.append(['APPEND'])
print(f"{list3} - we added APPEND to list1, but list3 didn't copied that")

list1[2][0] = 'c'
list1[4][0] = 'e'
list1[5][0] = 'f'

print(f"{list3} - we changed list1, and it affected list3")
print('')
list1.remove(['4'])
print(list1)
print('')

# deep copy
list4 = copy.deepcopy(list1)
list1.append(['ORIGINAL'])
list4.append(['DEEP COPY'])
list1[2][0] = 'LKJHGF'
list1[4][0] = 'JHVC'
list1[5][0] = 'OIY'
print(list1)
print(list4)