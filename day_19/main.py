import json
import re

# def lines_and_words_counter(file_path):
#     with open(file_path, 'r') as file:
#         print(f'File: {file_path}')
#         content = file.read()
#         # Count lines
#         lines = content.splitlines()
#         no_of_lines = len(lines)
#         print(f'Number of lines: {no_of_lines}')
#         # Count words
#         words = content.split()
#         no_of_words = len(words)
#         print(f'Number of words: {no_of_words}')
#         print()

# lines_and_words_counter('data/obama_speech.txt')
# lines_and_words_counter('data/michelle_obama_speech.txt')
# lines_and_words_counter('data/donald_speech.txt')
# lines_and_words_counter('data/melina_trump_speech.txt')

# def most_spoken_languages(filename, number_of_languages=10):
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = json.load(file)
    
#     languages = {}
#     for country in data:
#         for language in country['languages']:
#             if language not in languages:
#                 languages[language] = 1
#             else:
#                 languages[language] += 1
    
#     sorted_languages = sorted(languages.items(), key = lambda x: x[1], reverse=True)
#     top_languages = [(count, lang) for lang, count in sorted_languages[:number_of_languages]]
#     return top_languages

# print(most_spoken_languages('data/countries_data.json', 10))

# def most_populated_countries(filename, number_of_countries=10):
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = json.load(file)

#     countries = []
#     for country in data:
#         name = country['name']
#         population = country['population']
#         countries.append({'country': name, 'population': population})

#     countries

#     return countries[:number_of_countries]

# print(most_populated_countries('./data/countries_data.json', 10))

# def extract_incoming_emails(filename):
#     incoming_emails = []
#     pattern = re.compile(r'^From:\s*(\S+@\S+)')

#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             match = pattern.match(line)
#             if match:
#                 email = match.group(1)
#                 incoming_emails.append(email)
    
#     return incoming_emails

# print(extract_incoming_emails('data/email_exchanges_big.txt'))

# def find_most_common_words(filename, number_of_words=10):
#     with open(filename, 'r', encoding='utf-8') as file:
#         content = file.read()
    
#     words = re.findall(r'\b[a-zA-Z]+\b', content.lower())
#     word_count = {}
#     for word in words:
#         if word not in word_count:
#             word_count[word] = 1
#         else:
#             word_count[word] += 1

#     sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
#     return sorted_words[:number_of_words]
    
# print(find_most_common_words('data/sample.txt', 10))

# print(find_most_common_words('data/obama_speech.txt', 10))
# print(find_most_common_words('data/michelle_obama_speech.txt', 10))
# print(find_most_common_words('data/donald_speech.txt', 10))
# print(find_most_common_words('data/melina_trump_speech.txt', 10))

# print(find_most_common_words('data/romeo_and_juliet.txt', 10))
