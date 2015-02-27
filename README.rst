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

date_to_dayperiod
    Takes a date and returns 0 (morning), 1 (afternoon), 2 (evening) or 3 (night).

date_to_weekperiod
    Takes a date and returns the period of the week, (0-27).

weekperiod_to_dayperiod
    Takes a weekperiod (0-27) and returns the period of the day (0-3).

weekperiod_to_dayperiodname
    Takes a weekperiod (0-27) and returns 'Morning', 'Afternoon' ..

weekperiod_to_weekday
    Takes a weekperiod (0-27) and 0-6 (0 being Monday, 6 being Sunday)

weekperiod_to_weekdayname
    Takes a weekperiod (0-27) and returns 'Monday', 'Tuesday' ..

weekperiod_to_string
    Takes a weekperiod (0-27) and returns 'Sunday Night', 'Monday Morning' ..

weekperiod_is_monday
    Takes a weekperiod (0-27) and returns true if it's Monday.

weekperiod_is_tuesday
    ...

weekperiod_is_night
    Takes a weekperiod (0-27) and returns true if it's night.

weekperiod_is_morning
    Takes a weekperiod (0-27) and returns true if it's morning.

weekperiod_is_afternoon
    Takes a weekperiod (0-27) and returns true if it's afternoon.

weekperiod_is_evening
    Takes a weekperiod (0-27) and returns true if it's evening.

weekperiods_to_int(weekperiods)
    Takes a list of weekperiods and returns them in a 4-byte int suitable for
    storing.

weekperiod_is_set(weekperiod, compressed_int)
    Takes an weekperiod and returns true if the bit is set in compressed_int
    (see weekperiods_to_int).
