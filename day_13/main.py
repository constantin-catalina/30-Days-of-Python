numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [ number for row1 in list_of_lists for row2 in row1 for number in row2]
print(flattened_list)

numbers2 = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(numbers2)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3], capital.upper()] for country_list in countries for country, capital in country_list]
print(flattened_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries2 = [{'country': country.upper(), 'capital': capital.upper()} for country_list in countries for country, capital in country_list]
print(flattened_countries2)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flattened_names = [name + ' ' + surname for name_list in names for name, surname in name_list]
print(flattened_names)

solve_slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'undefined'
print(solve_slope(2, 4, 3, 5))