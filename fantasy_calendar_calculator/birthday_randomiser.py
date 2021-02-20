import random

def random_month(months_of_year):
    """
    Picks a random month from the given selection
    :param months_of_year:
    :return: an integer corresponding to the month of the year
    """
    rand_month_index = random.randint(1, months_of_year)

    return rand_month_index


def random_day(days_of_month):
    """
    Picks a random day within the given month
    :param days_of_month:
    :return: an integer corresponding to the day of the month
    """

    rand_day_index = random.randint(1, days_of_month)

    return rand_day_index

months = {'Dawn-Break': 27, 'Dawn-Rise': 28, 'Dawn-Peak': 28, 'High-Star': 30, 'Summer-Sun': 31, 'High-Fall': 30, 'Dusk-Peak': 28, 'Dusk-Rise': 28, 'Dusk-Break': 28, 'Winter-Way': 27, 'Winter-Peak': 27}

#months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}


days_in_year = sum(months.values())

month_names = list(months.keys())
month_days = list(months.values())

with open('new_names.txt', 'r') as g:
    with open('birthday_list.txt', 'a') as f:
        for character_name in g:
            character_name = character_name.rstrip()
            if not character_name: continue

            rand_month = random_month(len(month_names))

            rand_day = random_day(month_days[rand_month-1])

            with open('birthday_list.txt', 'a') as f:
                f.write('The birthday of ' + str(character_name) + ' is.\n')
                f.write('The ' + str(rand_day) + ' day in the month of ' + str(month_names[rand_month-1]) + '.\n\n')

