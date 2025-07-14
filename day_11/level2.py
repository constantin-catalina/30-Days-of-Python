import math

def evens_and_odds(num):
    odd = even = num // 2
    if num % 2 == 0:
        even += 1
    print(f'The number of odds are {odd}.\nThe number of evens are {even}.')

# evens_and_odds(100)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
# print(factorial(5))

def is_empty(param):
    return not param

# print(is_empty([]))

def calculate_mean(num):
    return sum(num) / len(num)

def calculate_median(num):
    num = sorted(num)
    n = len(num)
    mid = n // 2
    if n % 2 == 0:
        return (num[mid - 1] + num[mid]) / 2
    else:
        return num[mid]

def calculate_mode(num):
    frequency = {}
    max_freq = -1
    for x in num:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1
        
        if(max_freq < frequency[x]):
            max_freq = frequency[x]

    modes = [n for n, freq in frequency.items() if freq == max_freq]

    if len(modes) == len(num):
        return None
    
    return modes if len(modes) > 1 else modes[0]
    
def calculate_range(num):
    return max(num) - min(num)

def calculate_variance(num):
    mean = calculate_mean(num)
    return sum((x - mean) ** 2 for x in num) / len(num)

def calculate_std(num):
    variance = calculate_variance(num)
    return math.sqrt(variance)

data = [2, 4, 4, 4, 5, 5, 7, 9]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))
