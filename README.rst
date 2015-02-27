weekperiod
==========

Divides a week into 28 periods::

    0 is Sunday night
    1 is Monday morning
    2 is Monday afternoon
    3 is Monday evening
    4 is Monday night
    5 is Tuesday morning
    ...
    27 is Sunday evening

Functions
---------

date_to_dayperiod
    Takes a date and returns 0 (morning), 1 (afternoon), 2 (evening) or 3 (night).

date_to_weekperiod
    Takes a date and returns the period of the week, (0-27).

weekperiod_to_dayperiod
    Takes a weekperiod (0-27) and returns the period of the day (0-3).

weekperiod_to_dayperiodname
    Takes a weekperiod and returns 'Morning', 'Afternoon' ..

weekperiod_to_weekday
    Takes a weekperiod and 0-6 (0 being Monday, 6 being Sunday)

weekperiod_to_weekdayname
    Takes a weekperiod and returns 'Monday', 'Tuesday' ..

weekperiod_to_string
    Takes a weekperiod and returns 'Sunday Night', 'Monday Morning' ..

weekperiod_is_monday
    Takes a weekperiod and returns true if it's Monday.

weekperiod_is_tuesday
    See weekperiod_is_monday. These continue for every day of the week.

weekperiod_is_night
    Takes a weekperiod and returns true if it's night.

weekperiod_is_morning
    Takes a weekperiod and returns true if it's morning.

weekperiod_is_afternoon
    Takes a weekperiod and returns true if it's afternoon.

weekperiod_is_evening
    Takes a weekperiod and returns true if it's evening.

weekperiods_to_int(weekperiods)
    Takes a list of weekperiods and returns them in a 4-byte int suitable for
    storing.

weekperiod_is_set(weekperiod, compressed_int)
    Takes an weekperiod and returns true if the bit is set in compressed_int
    (see weekperiods_to_int).

Filtering by weekperiod with sqlalchemy
---------------------------------------

Store a list of periods in an integer column of a database table::

    class Meeting(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        periods = db.Column(db.Integer, nullable=True)

    meeting = Meeting()
    meeting.periods = weekperiods_to_int([0, 5, 27])
    meeting.store()

Then to select only records set for Sunday Evenings (27)::

```python
    Meeting.query.filter(Meeting.periods.op('&')(weekperiods_to_int([27])) > 0)
