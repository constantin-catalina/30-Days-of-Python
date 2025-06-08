# Day 2: 30 Days of python programming

first_name = 'John'
last_name = 'Rockson'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'New York'
age = 30
year = 1990
is_married = True
is_true = True
is_light_on = False

youngest_child, middle_child, oldest_child = ['Jane', 'Doe', 'Smith']
print('Middle child:', middle_child)
print()

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(youngest_child))
print(type(middle_child))
print(type(oldest_child))
print()

print(len(first_name))
print(len(first_name) == len(last_name))
print()

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

circle_radius = 30
area_of_circle = 3.14 * (circle_radius ** 2)
circum_of_circle = 2 * 3.12 * circle_radius
radius = float(input('Enter the radius of the circle: '))
area = 3.14 * (radius ** 2)
print('Area of the circle with radius', radius, 'is:', area)
print()

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = int(input('Enter your age: '))
print('Hi, I am ' + first_name + ' ' + last_name + '. I am ' + str(age) + ' years old and I live in ' + country + '.')
print()