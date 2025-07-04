from datetime import datetime, date, time, timedelta

now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()

print(f'Current date: {current_day}/{current_month}/{current_year} {current_hour}:{current_minute}')
print(f'Timestamp: {current_timestamp}')
print()

formatted_date = now.strftime('%d/%m/%Y %H:%M')
print(f'Formatted date: {formatted_date}')
print()

time_string = '5 December, 2019'
converted_time = datetime.strptime(time_string, '%d %B, %Y')
print(f'Converted time: {converted_time}')
print()

now = datetime.now()
new_year = datetime(year = 2026, month = 1, day = 1)
time_left_until_new_year = new_year - now
print(f'Time left until New Year: {time_left_until_new_year}')

date2 = datetime.strptime('1 January 1970', '%d %B %Y')
time_difference = now - date2
print(f'Time difference from 1 January 1970: {time_difference}')