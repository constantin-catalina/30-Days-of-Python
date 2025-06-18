concatenated_string = 'Thirty' + ' Days' + ' of' + ' Python'
print(concatenated_string)

concatenated_string2 = 'Coding' + ' For' + ' All'
print(concatenated_string2)

company = "Coding For All"
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())  
print(company.swapcase())

space_index = company.index(' ')
print(company[space_index + 1:])

try:
    company.index('Coding')
    print(True)
except ValueError:
    print(False)
    
print(True if company.find('Coding') != -1 else False)

print(company.replace('Coding', 'Python'))

python_string = 'Python for Everyone'
print(python_string.replace('Everyone', 'All'))

split_string = company.split()
print(split_string)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_list = companies.split(', ')
print(companies_list)

print(company[0])

last_index = len(company) - 1
print(last_index)

print(company[10])

def abreviation(string):
    words = string.split()
    abbreviation = ''.join(word[0].upper() for word in words)
    return abbreviation

string1 = 'Python For Everyone'
print(abreviation(string1))

string2 = 'Coding For All'
print(abreviation(string2))

try:
    index = company.index('C')
    print(index)
except ValueError:
    print('Character not found')

string3 = 'Coding For All People'
print(string3.rfind('l'))

string4 = 'You cannot end a sentence with because because because is a conjunction'
print(string4.find('because'))

try:
    idx = string4.rindex('because')
    print(idx)
except ValueError:
    print('Substring not found')

result = string4.replace('because because because ', '')
print(result)

print(company.startswith('Coding'))
print(company.endswith('coding'))

string5 = '   Coding For All   '
print(string5.strip())

string6 = '30 Days Of Python'
print(string6.isidentifier())

string7 = 'thirty_days_of_python'
print(string7.isidentifier())

list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list2 = '# '.join(list1)
print(list2)

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
print()

radius = 10
area = 3.14 * radius ** 2
print('radius = {}'.format(radius))
print('area = {} * radius ** {}'.format(3.14, 2))
print('The area of a circle with radius {} is {}'.format(radius, area))

a = 8
b = 6
print('a + b = {}'.format(a + b))
print('a - b = {}'.format(a - b))
print('a * b = {}'.format(a * b))
print('a / b = {:.2f}'.format(a / b))
print('a % b = {}'.format(a % b))
print('a // b = {}'.format(a // b))
print('a ** b = {}'.format(a ** b))