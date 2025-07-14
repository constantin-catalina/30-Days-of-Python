import math
import cmath

def add_two_numbers(a, b):
    if isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex)):
        return a + b
    else:
        raise TypeError("Both inputs must be numbers!")

# print(add_two_numbers(5, 3))

def area_of_circle(r):
    return math.pi * r * r

# print(area_of_circle(10))

def add_all_nums(*num_list):
    total = 0
    for x in num_list:
        if isinstance(x, (int, float, complex)):
            total += x
        else:
            raise TypeError("Arguments must be numbers!")
    return total

# print(add_all_nums(1, 2, 3, 4, 5))

def convert_celcius_to_fehrenheit(temp):
    fhr_temp = temp * 9 / 5 + 32
    return fhr_temp

# print(convert_celcius_to_fehrenheit(20))

def check_season(month):
    month = month.strip().lower()

    if month in ('september', 'october', 'november'):
        return 'Autumn'
    elif month in ('december', 'january', 'february'):
        return 'Winter'
    elif month in ('march', 'april', 'may'):
        return 'Spring'
    elif month in ('june', 'july', 'august'):
        return 'Summer'
    else:
        return 'Invalid month'

# print(check_season("March"))

def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError('Slope is undefined')
    return (y2 - y1) / (x2 - x1)

# print(calculate_slope(1, 2, 3, 6))

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        if b == 0:
            if c != 0:
                return "No solution!"
            else:
                return "Infinite solutions!"
        return [-c / b]
    
    discr = b ** 2 - 4 * a * c

    if discr > 0:
        root1 = (-b + math.sqrt(discr)) / (2 * a)
        root2 = (-b - math.sqrt(discr)) / (2 * a)
        return [root1, root2]
    elif discr == 0:
        root = -b / (2 * a)
        return [root]
    else:
        # Complex roots
        root1 = (-b + cmath.sqrt(discr)) / (2 * a)
        root2 = (-b - cmath.sqrt(discr)) / (2 * a)
        return [root1, root2]
    
# print(solve_quadratic_eqn(1, -3, 2))    
# print(solve_quadratic_eqn(1, 2, 1))     
# print(solve_quadratic_eqn(1, 0, 1))     
# print(solve_quadratic_eqn(0, 2, -4))    

def print_list(lista):
    for x in lista:
        print(x)

# print_list([1, 2, 3, 4, 5])

def reverse_list(lista):
    rev = []
    for x in lista:
        rev.insert(0, x)
    return rev

# print(reverse_list(['A', 'B', 'C']))

def capitalize_list_items(lista):
    return [str(x).capitalize() for x in lista]

# print(capitalize_list_items(['apple', 'bANAna', 'CHERRY']))

def add_item(lista, item):
    l = lista.copy()
    l.append(item)
    return l

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))

def remove_item(lista, item):
    l = lista.copy()
    l.remove(item)
    return l

# print(remove_item(food_staff, 'Mango'))

def sum_of_numbers(param):
    total = 0
    for i in range(param + 1):
        total += i

    return total

# print(sum_of_numbers(10))

def sum_of_odds(param):
    total = 0
    for i in range(param + 1):
        if i % 2 != 0:
            total += i

    return total

# print(sum_of_odds(5))

def sum_of_even(param):
    total = 0
    for i in range(param + 1):
        if i % 2 == 0:
            total += i

    return total

# print(sum_of_even(5))
