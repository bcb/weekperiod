"""period.py

weekperiod: Time of the week between 0 (Sunday Night) and 27 (Sunday Evening)
dayperiod: Time of the day between 0 (Night) and 3 (Evening)
"""

from datetime import datetime
from math import floor


weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', \
    'Saturday', 'Sunday']

dayperiod_names = ['Night', 'Morning', 'Afternoon', 'Evening']


def date_to_dayperiod(date=None):
    """Returns the period of the day, between 0 (Night) and 3 (Evening)"""

    if date is None:
        date = datetime.now()

    return floor(date.hour / 6)


def date_to_weekperiod(date=None):
    """Returns the period of the week, between 0 (Sunday night) and 27 (Sunday
    Evening)"""

    if date is None:
        date = datetime.now()

    return floor((date.weekday() * 4) + date_to_dayperiod(date))


def weekperiod_to_dayperiod(weekperiod):
    """Returns the dayperiod (0-3) given a weekperiod"""

    return floor(weekperiod % 4)


def weekperiod_to_dayperiodname(weekperiod):
    """Returns the day period name (Night/Morning/Afternoon/Evening), given a
    weekperiod"""

    return dayperiod_names[weekperiod_to_dayperiod(weekperiod)]


def weekperiod_to_weekday(weekperiod):
    """Returns the weekday (0-6) given a weekperiod"""

    # 0 is Sunday night
    if weekperiod == 0:
        return 6
    else:
        return floor((weekperiod - 1) / 4)


def weekperiod_to_weekdayname(weekperiod):
    """Returns the weekday name (eg. Monday), given a weekperiod"""

    return weekday_names[weekperiod_to_weekday(weekperiod)]


def weekperiod_to_string(weekperiod):
    """Returns a description, eg. 'Sunday Night', given a weekperiod"""

    return '{} {}'.format(weekperiod_to_weekdayname(weekperiod), \
        weekperiod_to_dayperiodname(weekperiod))


def weekperiods_to_int(weekperiods):
    """Takes a list of weekperiods, and compresses them into a 4-byte int"""

    x = 0
    for i in weekperiods:
        x = x | (1 << i)
    return x


def weekperiod_is_set(weekperiod, compressed_int):
    """Returns true if a period bit is set in a compressed int"""

    return (1 << weekperiod) & compressed_int


def weekperiod_is_monday(weekperiod):
    """Returns true if it's Monday"""

    return weekperiod_to_weekday(weekperiod) == 0


def weekperiod_is_tuesday(weekperiod):
    """Returns true if it's Tuesday"""

    return weekperiod_to_weekday(weekperiod) == 1


def weekperiod_is_wednesday(weekperiod):
    """Returns true if it's Wednesday"""

    return weekperiod_to_weekday(weekperiod) == 2


def weekperiod_is_thursday(weekperiod):
    """Returns true if it's Tuesday"""

    return weekperiod_to_weekday(weekperiod) == 3


def weekperiod_is_friday(weekperiod):
    """Returns true if it's Friday"""

    return weekperiod_to_weekday(weekperiod) == 4


def weekperiod_is_saturday(weekperiod):
    """Returns true if it's Saturday"""

    return weekperiod_to_weekday(weekperiod) == 5


def weekperiod_is_sunday(weekperiod):
    """Returns true if it's Sunday"""

    return weekperiod_to_weekday(weekperiod) == 6


def weekperiod_is_night(weekperiod):
    """Returns true if it's night"""

    return weekperiod_to_dayperiod(weekperiod) == 0


def weekperiod_is_morning(weekperiod):
    """Returns true if it's morning"""

    return weekperiod_to_dayperiod(weekperiod) == 1


def weekperiod_is_afternoon(weekperiod):
    """Returns true if it's afternoon"""

    return weekperiod_to_dayperiod(weekperiod) == 2


def weekperiod_is_evening(weekperiod):
    """Returns true if it's evening"""

    return weekperiod_to_dayperiod(weekperiod) == 3
