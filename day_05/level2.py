ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print('Sorted ages:', ages)
print('Min age:', min(ages))
print('Max age:', max(ages))

ages.insert(0, min(ages))
ages.append(max(ages))
print('Updated ages:', ages)

middle_index = len(ages) // 2
if len(ages) % 2 == 0:
    median = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median = ages[middle_index]

print('Median age:', median)

average_age = sum(ages) / len(ages)
print('Average age:', average_age)

range_age = max(ages) - min(ages)
print('Range of ages:', range_age)

print('Is the average age closer to the minimum age?', abs(min(ages) - average_age) < abs(max(ages) - average_age))

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

middle_index = len(countries) // 2

if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = [countries[middle_index]]

print('Middle country/countries:', middle_countries)

if len(countries) % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else:
    first_half = countries[:middle_index]
    second_half = countries[middle_index + 1:]

countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic_countries = countries2
print('Country 1:', country1)
print('Country 2:', country2)
print('Country 3:', country3)
print('Scandic countries:', scandic_countries) 