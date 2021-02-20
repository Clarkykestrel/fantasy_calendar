import random
#import sys

months = {'Dawn-Break': 27, 'Dawn-Rise': 28, 'Dawn-Peak': 28, 'High-Star': 30, 'Summer-Sun': 31, 'High-Fall': 30, 'Dusk-Peak': 28, 'Dusk-Rise': 28, 'Dusk-Break': 28, 'Winter-Way': 27, 'Winter-Peak': 27}

days_in_year = sum(months.values())

month_names = list(months.keys())
month_days = list(months.values())

with open('new_names.txt', 'r') as g:
    with open('birthday_list.txt', 'a') as f:
        for character_name in g:
            character_name = character_name.rstrip()
            if not character_name: continue

            rand_month = random.randint(1, len(month_names))
            rand_month_index = rand_month - 1

            rand_month_length = month_days[rand_month_index]

            rand_day = random.randint(1, rand_month_length)

            #print('The ' + str(rand_day) + ' day in the month of ' + str(month_names[rand_month_index]) + '.')
            #character_name = sys.argv[1]
            with open('birthday_list.txt', 'a') as f:
                f.write('The birthday of ' + str(character_name) + ' is.\n')
                f.write('The ' + str(rand_day) + ' day in the month of ' + str(month_names[rand_month_index]) + '.\n\n')
