"""promo_test.py"""
#pylint:disable=missing-docstring,line-too-long,wildcard-import,unused-wildcard-import

from unittest import TestCase
from datetime import datetime

from weekperiod import *

class TestPeriod(TestCase):
    #pylint:disable=no-init

    def test_date_to_dayperiod(self):
        self.assertEqual(0, date_to_dayperiod(datetime(2015, 1, 1, 0)))
        self.assertEqual(1, date_to_dayperiod(datetime(2015, 1, 1, 6)))
        self.assertEqual(2, date_to_dayperiod(datetime(2015, 1, 1, 12)))
        self.assertEqual(3, date_to_dayperiod(datetime(2015, 1, 1, 18)))

    def test_date_to_weekperiod(self):
        self.assertTrue(date_to_weekperiod() in range(28)) # Current time
        self.assertEqual(27, date_to_weekperiod(datetime(2015, 1, 4, 23))) # Sunday evening
        self.assertEqual(0, date_to_weekperiod(datetime(2015, 1, 5, 0))) # Sunday night

    def test_weekperiod_to_dayperiod(self):
        self.assertEqual(0, weekperiod_to_dayperiod(0))
        self.assertEqual(1, weekperiod_to_dayperiod(1))
        self.assertEqual(2, weekperiod_to_dayperiod(2))
        self.assertEqual(3, weekperiod_to_dayperiod(3))
        self.assertEqual(0, weekperiod_to_dayperiod(4))
        self.assertEqual(1, weekperiod_to_dayperiod(5))
        self.assertEqual(3, weekperiod_to_dayperiod(27))

    def test_weekperiod_to_dayperiodname(self):
        self.assertEqual('Night', weekperiod_to_dayperiodname(0))
        self.assertEqual('Morning', weekperiod_to_dayperiodname(1))
        self.assertEqual('Afternoon', weekperiod_to_dayperiodname(2))
        self.assertEqual('Evening', weekperiod_to_dayperiodname(3))
        self.assertEqual('Night', weekperiod_to_dayperiodname(4))
        self.assertEqual('Morning', weekperiod_to_dayperiodname(5))
        self.assertEqual('Evening', weekperiod_to_dayperiodname(27))

    def test_weekperiod_to_weekday(self):
        self.assertEqual(6, weekperiod_to_weekday(0))
        self.assertEqual(0, weekperiod_to_weekday(1))
        self.assertEqual(0, weekperiod_to_weekday(2))
        self.assertEqual(0, weekperiod_to_weekday(3))
        self.assertEqual(0, weekperiod_to_weekday(4))
        self.assertEqual(1, weekperiod_to_weekday(5))
        self.assertEqual(6, weekperiod_to_weekday(27))

    def test_weekperiod_to_weekdayname(self):
        self.assertEqual('Sunday', weekperiod_to_weekdayname(0))
        self.assertEqual('Monday', weekperiod_to_weekdayname(1))
        self.assertEqual('Monday', weekperiod_to_weekdayname(2))
        self.assertEqual('Monday', weekperiod_to_weekdayname(3))
        self.assertEqual('Monday', weekperiod_to_weekdayname(4))
        self.assertEqual('Tuesday', weekperiod_to_weekdayname(5))
        self.assertEqual('Sunday', weekperiod_to_weekdayname(27))

    def test_weekperiod_to_string(self):
        self.assertEqual(weekperiod_to_string(0), 'Sunday Night')
        self.assertEqual(weekperiod_to_string(1), 'Monday Morning')
        self.assertEqual(weekperiod_to_string(2), 'Monday Afternoon')
        self.assertEqual(weekperiod_to_string(3), 'Monday Evening')
        self.assertEqual(weekperiod_to_string(4), 'Monday Night')
        self.assertEqual(weekperiod_to_string(5), 'Tuesday Morning')
        self.assertEqual(weekperiod_to_string(27), 'Sunday Evening')

    def test_weekperiods_to_int(self):
        self.assertEqual(0b1, weekperiods_to_int([0]))
        self.assertEqual(0b10, weekperiods_to_int([1]))
        self.assertEqual(0b100011, weekperiods_to_int([0, 1, 5]))
        self.assertEqual(0b1000000000000000000000000001, weekperiods_to_int([0, 27]))

    def test_weekperiod_is_monday(self):
        self.assertFalse(weekperiod_is_monday(0))
        self.assertTrue(weekperiod_is_monday(1))
        self.assertTrue(weekperiod_is_monday(2))
        self.assertTrue(weekperiod_is_monday(3))
        self.assertTrue(weekperiod_is_monday(4))
        self.assertFalse(weekperiod_is_monday(5))
        self.assertFalse(weekperiod_is_monday(27))

    def test_weekperiod_is_tuesday(self):
        self.assertFalse(weekperiod_is_tuesday(0))
        self.assertTrue(weekperiod_is_tuesday(5))
        self.assertFalse(weekperiod_is_tuesday(27))

    def test_weekperiod_is_wednesday(self):
        self.assertFalse(weekperiod_is_wednesday(0))
        self.assertTrue(weekperiod_is_wednesday(9))
        self.assertFalse(weekperiod_is_wednesday(27))

    def test_weekperiod_is_thursday(self):
        self.assertFalse(weekperiod_is_thursday(0))
        self.assertTrue(weekperiod_is_thursday(13))
        self.assertFalse(weekperiod_is_thursday(27))

    def test_weekperiod_is_friday(self):
        self.assertFalse(weekperiod_is_friday(0))
        self.assertTrue(weekperiod_is_friday(17))
        self.assertFalse(weekperiod_is_friday(27))

    def test_weekperiod_is_saturday(self):
        self.assertFalse(weekperiod_is_saturday(0))
        self.assertTrue(weekperiod_is_saturday(21))
        self.assertFalse(weekperiod_is_saturday(27))

    def test_weekperiod_is_sunday(self):
        self.assertTrue(weekperiod_is_sunday(0))
        self.assertFalse(weekperiod_is_sunday(24))
        self.assertTrue(weekperiod_is_sunday(25))
        self.assertTrue(weekperiod_is_sunday(26))
        self.assertTrue(weekperiod_is_sunday(27))

    def test_weekperiod_is_night(self):
        self.assertTrue(weekperiod_is_night(0))
        self.assertFalse(weekperiod_is_night(1))
        self.assertFalse(weekperiod_is_night(2))
        self.assertFalse(weekperiod_is_night(3))
        self.assertTrue(weekperiod_is_night(4))
        self.assertFalse(weekperiod_is_night(5))
        self.assertFalse(weekperiod_is_night(27))

    def test_weekperiod_is_morning(self):
        self.assertFalse(weekperiod_is_morning(0))
        self.assertTrue(weekperiod_is_morning(1))
        self.assertFalse(weekperiod_is_morning(2))
        self.assertFalse(weekperiod_is_morning(3))
        self.assertFalse(weekperiod_is_morning(4))
        self.assertTrue(weekperiod_is_morning(5))
        self.assertFalse(weekperiod_is_morning(27))

    def test_weekperiod_is_afternoon(self):
        self.assertFalse(weekperiod_is_afternoon(0))
        self.assertFalse(weekperiod_is_afternoon(1))
        self.assertTrue(weekperiod_is_afternoon(2))
        self.assertFalse(weekperiod_is_afternoon(3))
        self.assertFalse(weekperiod_is_afternoon(4))
        self.assertFalse(weekperiod_is_afternoon(5))
        self.assertFalse(weekperiod_is_afternoon(27))

    def test_weekperiod_is_evening(self):
        self.assertFalse(weekperiod_is_evening(0))
        self.assertFalse(weekperiod_is_evening(1))
        self.assertFalse(weekperiod_is_evening(2))
        self.assertTrue(weekperiod_is_evening(3))
        self.assertFalse(weekperiod_is_evening(4))
        self.assertFalse(weekperiod_is_evening(5))
        self.assertTrue(weekperiod_is_evening(27))
