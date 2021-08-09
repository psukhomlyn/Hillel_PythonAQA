"""
Реализовать функцию которая возвращает дату недельной давности от
текущего момента времени.
"""


from datetime import date, timedelta


def week_ago_date():
    """
    Return time 1 week ago
    """
    week_ago = date.today() - timedelta(7)
    return week_ago


print(week_ago_date())