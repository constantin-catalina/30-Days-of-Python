import math
import keyword
from data.countries_data import countries_data

def is_prime(x):
    for i in range (2, x):
        if x % i == 0:
            return False
    return True

# print(is_prime(5))
# print(is_prime(9))

def is_unique(lista):
    i = 1
    for x in lista:
        if x in lista[i:]:
            return False
        i += 1

# print(is_unique([1, 2, 3, 4, 5]))
# print(is_unique([1, 2, 3, 4, 6 , 2, 4]))

def check_datatype(lista):
    data_type = type(lista[0])
    for x in lista:
        if not isinstance(x, data_type):
            return False
    return True

# print(check_datatype(["Hi", "Bye", 5]))
# print(check_datatype(["Hi", "Bye", "Ciao"]))

def check_valid_variable(item):
    return item.isidentifier() and not keyword.iskeyword(item)

# print(check_valid_variable("my_var"))
# print(check_valid_variable("def"))
# print(check_valid_variable("2025var"))

def most_spoken_languages(data, top_n = 10):
    language_count = {}

    for country in data:
        for language in country.get('languages', []):
            language_count[language] = language_count.get(language, 0) + 1

    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_languages[:top_n]

print("Top 10 most spoken languages:")
print(most_spoken_languages(countries_data, top_n=10))

def most_populated_countries(data, top_n = 10):
    sorted_countries = sorted(countries_data, key=lambda c: c.get('population', 0), reverse=True)
    result = [{"country": country["name"], "population": country["population"]} for country in sorted_countries[:top_n]]
    return result

print("\nTop 10 most populated countries:")
print(most_populated_countries(countries_data, top_n=10))