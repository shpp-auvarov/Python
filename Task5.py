from datetime import datetime
from datetime import timedelta

now = datetime.now()
increased_date = now + timedelta(days=1)
print(now, 'Time now')
print(increased_date, 'The time after adding 1 day')

new_date_str = increased_date.strftime("%d-%m-%y %H:%S")
print(new_date_str, 'Time now')

variable_str = '2020-02-03 09:18:36.000'

datetime_var = datetime.strptime(variable_str, '%Y-%m-%d %H:%M:%S.%f')
print(datetime_var)

print(datetime_var.strftime('%d'), 'Day')
print(datetime_var.strftime('%m'), 'Month')
print(datetime_var.strftime('%Y'), 'Year')
print(datetime_var.strftime('%H'), 'Hours')
print(datetime_var.strftime('%S'), 'Seconds')

import random

# Print of 3 random numbers that are divisible by 5 without remainder
for i in range(1, 4):
    print('Number', i, '=', random.randrange(100, 999, 5))

# Generate a random string from initial string with 10 digits length
str = '12345678'
if str.__len__() < 10:
    for i in range(0, 10 - str.__len__()):
        str += random.choice(str)
random_str = random.sample(str, 10)
print(''.join(random_str), 'random string')

# Generate 100 string tickets and choose 2 winner tickets
list_of_tickets = []
for i in range(0, 100):
    ticket = ""
    for j in range(0, 10):
        digit = random.randint(0, 9)
        ticket += f'{digit}'
    list_of_tickets.append(ticket)
winning_ticket_1 = random.choice(list_of_tickets)
list_of_tickets.remove(winning_ticket_1)
winning_ticket_2 = random.choice(list_of_tickets)
print(winning_ticket_1, 'winning ticket')
print(winning_ticket_2, 'winning ticket')


def throw_exception(a, b):
    return a / b


try:
    throw_exception(2, 0)
    print("Done")
except Exception as inst:
    print("Catch exception", type(inst))
    print(inst)
finally:
    print("Successful anyway")
