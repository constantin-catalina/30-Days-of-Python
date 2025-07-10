from data.stop_words import stop_words

import re
import math

def clean_text(text):
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

def check_text_similarity(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1 = text_to_vector(remove_support_words(clean_text(f1.read()), stop_words))
        text2 = text_to_vector(remove_support_words(clean_text(f2.read()), stop_words))
    return cosine_similarity(text1, text2)

def remove_support_words(text, support_words):
    filtered_text = ' '.join([word for word in text.split() if word not in support_words])
    return filtered_text

def text_to_vector(text):
    words = text.split()
    vector = {}
    for word in words:
        vector[word] = vector.get(word, 0) + 1
    return vector

def cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([v**2 for v in vec1.values()])
    sum2 = sum([v**2 for v in vec2.values()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    return round(numerator / denominator, 4) if denominator else 0.0

def main():
    file1 = 'data/michelle_obama_speech.txt'
    file2 = 'data/melina_trump_speech.txt'
    similarity = check_text_similarity(file1, file2)
    print("The similarity between the two texts is:", similarity)

main()