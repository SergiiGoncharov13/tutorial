from datetime import timedelta, date

users = [
    {"name": "Bill", "birthday": date(1992, 11, 18)},
    {"name": "Kate", "birthday": date(2000, 11, 20)},
    {"name": "John", "birthday": date(2001, 12, 14)},
    {"name": "Ann", "birthday": date(1999, 11, 13)},
    {"name": "Oleg", "birthday": date(2002, 11, 24)},
    {"name": "Vlad", "birthday": date(1995, 11, 15)},
    {"name": "Frank", "birthday": date(1999, 11, 16)}
]

today_date = date.today()
this_year = today_date.year
delta_1 = timedelta(days=5)
delta_2 = timedelta(days=2)


def get_birthdays_per_week(users):

    day_of_week = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }
    for user in users:
        if 'birthday' in user:
            new_date = user["birthday"].replace(year=this_year)
            if new_date <= (today_date + delta_1) and new_date >= (today_date - delta_2):
                if date.weekday(new_date) in (0, 5, 6):
                    day_of_week.get("monday").append(user.get("name"))
                elif date.weekday(new_date) == 1:
                    day_of_week.get("tuesday").append(user.get("name"))
                elif date.weekday(new_date) == 2:
                    day_of_week.get("wednesday").append(user.get("name"))
                elif date.weekday(new_date) == 3:
                    day_of_week.get("thursday").append(user.get("name"))
                elif date.weekday(new_date) == 4:
                    day_of_week.get("friday").append(user.get("name"))

    return print_result_list(day_of_week)


def print_result_list(day_of_week):
    for k, v in day_of_week.items():
        if v:
            print(f'{k}: {", ".join(v)}')


get_birthdays_per_week(users)
