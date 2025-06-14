import math

# age = 20
# height = 1.75
# complex_number = 3 + 4j

# triangle_base = float(input("Enter the base of the triangle: "))
# triangle_heigh = float(input("Enter the height of the triangle: "))
# triangle_area = triangle_base * triangle_heigh * 0.5
# print("The are of the triangle is ", triangle_area)
# print()

# side_a = float(input("Enter side a: "))
# side_b = float(input("Enter side b: "))
# side_c = float(input("Enter side c: "))
# perimeter = side_a + side_b + side_c
# print("The perimeter of the triangle is ", perimeter)
# print()

# rectangle_length = float(input("Enter the length of the rectangle: "))
# rectangle_width = float(input("Enter the width of the rectangle: "))
# rectangle_area = rectangle_length * rectangle_width
# print("The area of the rectangle is ", rectangle_area)
# perimeter_rectangle = 2 * (rectangle_length + rectangle_width)
# print("The perimeter of the rectangle is ", perimeter_rectangle)
# print()

# radius = float(input("Enter the radius of the circle: "))
# circle_area = 3.14 * radius ** 2
# print("The area of the circle is ", circle_area)
# print()

# slope_1 = 2
# b = -2
# x_intercept = -b / m
# y_intercept = b

# x1, y1 = 2, 2
# x2, y2 = 6, 10
# slope_2 = (y2 - y1) / (x2 - x1)
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# print(slope_1 > slope_2)

# x = 2
# y = x ** 2 + 6 * x + 9

# a = 1
# b = 6
# c = 9
# D = b**2 - 4*a*c

# if D >= 0:
#     x1 = (-b + math.sqrt(D)) / (2*a)
#     x2 = (-b - math.sqrt(D)) / (2*a)
#     if( x1 == x2):
#         print(f"The equation has one real root: x1 = x2 = {x1}")
#     else: 
#         print(f"Roots: x1 = {x1}, x2 = {x2}")
# else:
#     print("No real roots")
# print()

# print(len('python'))
# print(len('dragon'))
# print(len('python') != len('dragon'))

# print('on' in 'python' and 'on' in 'dragon')
# print('jargon' in 'I hope this course is not full of jargon')
# print('on' not in 'python' and 'on' not in 'dragon')
# print()

# float_length = float(len('python'))
# string_length = str(float_length)

# number = 12425
# print('Is even? ', number % 2 == 0)
# print('Is odd? ', number % 2 != 0)
# print()

print((7 // 3) == int(2.7))
print(type('10') is type(10))
print(int(float('9.8')) == 10)
print()

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
pay = hours * rate
print(f"Your weekly earning is {pay}")
print()

years = int(input("Enter number of years you have lived: "))
months = years * 12
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"You have lived for {seconds} seconds.")
print()

for i in range (1, 6):
    print(f'{i} {i**0} {i**1} {i**2} {i**3}')
print()