lst = []
lst2 = [1, 2, 3, 4, 5, 6, 7]

print(len(lst2))

print('first element:', lst2[0])
print('middle element:', lst2[len(lst2) // 2])
print('last element:', lst2[-1])

mixed_data_types = ['Vivi', 200, 1.00, False, 'Romania']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('Twitter')
it_companies.insert(len(it_companies) // 2, 'Snapchat')
print(it_companies)

it_companies[0] = it_companies[0].upper()
list2 = ('# ').join(it_companies)
print(list2)

print('Is Google in the list?', 'Google' in it_companies)

print(it_companies.sort())
it_companies.reverse()
print(it_companies)

del it_companies[0:3]
del it_companies[-3:]

if len(it_companies) % 2 == 0:
    middle_index = len(it_companies) // 2
    del it_companies[middle_index - 1:middle_index + 1]
else:
    middle_index = len(it_companies) // 2
    del it_companies[middle_index]

print(it_companies)

it_companies.pop(0)
it_companies.pop(-1)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

index = full_stack.index('Redux') + 1
full_stack.insert(index, 'Python')
full_stack.insert(index + 1, 'SQL')
print(full_stack)
