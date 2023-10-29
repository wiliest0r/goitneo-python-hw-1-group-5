''' 
This module provides time function 
for calculation dict with birthdays for current week.
'''
from datetime import datetime

users = [
    {
        "name": "Belly Taes",
        "birthday": datetime(1995, 1,   25)
    },
    {
        "name": "Tom Sonl",
        "birthday": datetime(1989, 2,   21)
    },
    {
        "name": "Joshua Harison",
        "birthday": datetime(1997, 8,   9)
    },
    {
        "name": "Tony Lourens",
        "birthday": datetime(2003, 10,   26)
    },
    {
        "name": "Jacob Marxon",
        "birthday": datetime(2001, 11,  8)
    },
    {
        "name": "Bill Gates",
        "birthday": datetime(1955, 10,  28)
    },
    {
        "name": "Bella Gadot",
        "birthday": datetime(2005, 10,  29)
    },
    {
        "name": "Phill Routhwood",
        "birthday": datetime(2005, 10,  30)
    }
]

today = datetime.today().date()


def get_birthdays_per_week(users_dict) -> dict:
    """Return the dict with name and birthdays for this week."""
    birthdays_this_week = {}
    for user in users_dict:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)
        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            weekday = birthday_this_year.strftime('%A')

            if birthday_this_year.weekday() >= 5:
                weekday = 'Monday'

            if weekday not in birthdays_this_week:
                birthdays_this_week[weekday] = [name]
            else:
                birthdays_this_week[weekday].append(name)
    return birthdays_this_week


result = get_birthdays_per_week(users)
for day, names in sorted(result.items()):  # відсортовано за днями тижня
    print(f"{day}: {', '.join(names)}")
