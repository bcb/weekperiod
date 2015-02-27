weekperiod
==========

Functions to divide a week into 28 periods.

Every weekday has 4 periods - morning, afternoon, evening and night::

    0 is Sunday night
    1 is Monday morning
    2 is Monday afternoon
    3 is Monday evening
    4 is Monday night
    5 is Tuesday morning
    ...
    27 is Sunday evening

date_to_dayperiod(date=None)
    Takes a date and returns 0 (morning), 1 (afternoon), 2 (evening) or 3 (night).

date_to_weekperiod(date=None)
    Takes a date and returns the period of the week, (0-27).

weekperiod_to_dayperiod(weekperiod)

weekperiod_to_dayperiodname(weekperiod)
weekperiod_to_weekday(weekperiod)
weekperiod_to_weekdayname(weekperiod)
weekperiod_to_string(weekperiod)

weekperiod_is_monday(weekperiod)
weekperiod_is_tuesday(weekperiod)
weekperiod_is_wednesday(weekperiod)
weekperiod_is_thursday(weekperiod)
weekperiod_is_friday(weekperiod)
weekperiod_is_saturday(weekperiod)
weekperiod_is_sunday(weekperiod)
weekperiod_is_night(weekperiod)
weekperiod_is_morning(weekperiod)
weekperiod_is_afternoon(weekperiod)
weekperiod_is_evening(weekperiod)

weekperiods_to_int(weekperiods)
weekperiod_is_set(weekperiod, compressed_int)
