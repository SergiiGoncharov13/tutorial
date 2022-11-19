from datetime import timedelta, datetime

users = [
    {"name": "Bill", "birthday": datetime(1992, 11, 23)},
    {"name": "Kate", "birthday": datetime(2000, 11, 22)},
    {"name": "John", "birthday": datetime(2001, 11, 24)},
    {"name": "Ann", "birthday": datetime(1999, 11, 23)},
    {"name": "Oleg", "birthday": datetime(2002, 12, 12)},
    {"name": "Vlad", "birthday": datetime(1995, 11, 30)},
    {"name": "Frank", "birthday": datetime(1999, 11, 16)}
]

today_date = datetime.now()
if today_date.weekday() == 5:
    days_interval = timedelta(days=6)
elif today_date.weekday() == 6:
    days_interval = timedelta(days=5)
else:
    days_interval = timedelta(days=7)
new_day = today_date + days_interval


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
        new_date = datetime(
            year=today_date.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )

        if today_date < new_date <= new_day:
            weekday_string = new_date.strftime("%A")
            if weekday_string in ["saturday", "sunday"]:
                weekday_string = "monday"
            day_of_week.get(weekday_string).append(user.get("name"))
    return print_result_list(day_of_week)


def print_result_list(day_of_week):
    for k, v in day_of_week.items():
        if v:
            print(f'{k}: {", ".join(v)}')



if __name__ == "__main__":
    get_birthdays_per_week(users)
