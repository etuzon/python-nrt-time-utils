from time import sleep

import pytest

from nrt_time_utils.time_utils import \
    TimeUtil, YMD_HMS_DATE_FORMAT, YMD_HMSF_DATE_FORMAT, YMD_Z_DATE_FORMAT
from tests.time_utils_data import \
    date_str_to_date_time_data, is_date_in_format_data, is_leap_year_data, \
    day_start_date_ms_data, day_end_date_ms_data, \
    timezone_date, date_str_to_date_ms_data


def test_date_ms_to_date_str():
    date_str = TimeUtil.date_ms_to_date_str(1609459200000, YMD_HMSF_DATE_FORMAT)
    assert date_str is not None


def test_date_ms_to_date_time():
    date_time = TimeUtil.date_ms_to_date_time(1609459200000, 'UTC')
    assert date_time
    assert date_time.year == 2021
    assert date_time.month == 1
    assert date_time.day == 1
    assert date_time.hour == 0
    assert date_time.minute == 0
    assert date_time.second == 0


@pytest.mark.parametrize(
    'date_str, date_format, expected_date_ms', date_str_to_date_ms_data)
def test_date_str_to_date_ms(date_str, date_format, expected_date_ms):
    date_ms = TimeUtil.date_str_to_date_ms(date_str, date_format)
    assert date_ms == expected_date_ms


def test_date_str_to_date_ms_unknown_timezone_negative():
    with pytest.raises(ValueError):
        TimeUtil.date_str_to_date_ms('2021-01-01 UNKNOWN', YMD_Z_DATE_FORMAT)


def test_date_str_to_date_ms_no_timezone_negative():
    with pytest.raises(ValueError):
        TimeUtil.date_str_to_date_ms('2021-01-01', YMD_Z_DATE_FORMAT)


@pytest.mark.parametrize(
    'date_str, date_format, expected_date_time', date_str_to_date_time_data)
def test_date_str_to_date_time(date_str, date_format, expected_date_time):
    dt = TimeUtil.date_str_to_date_time(date_str, date_format)
    assert dt == expected_date_time


def test_date_time_to_date_ms():
    date_time = TimeUtil.date_str_to_date_time(
        '2021-01-01 00:00:00', YMD_HMS_DATE_FORMAT)
    date_ms = TimeUtil.date_time_to_date_ms(date_time)
    assert date_ms


def test_get_current_date_ms():
    date_ms_1 = TimeUtil.get_current_date_ms()
    assert date_ms_1 > 0
    sleep(1)
    date_ms_2 = TimeUtil.get_current_date_ms()
    assert date_ms_1 < date_ms_2 < date_ms_1 + 5000


@pytest.mark.parametrize(
    'date_ms, expected_date_ms, tz', day_end_date_ms_data)
def test_get_day_end_date_ms(date_ms, expected_date_ms, tz):
    assert TimeUtil.get_day_end_date_ms(date_ms, tz) == expected_date_ms


@pytest.mark.parametrize(
    'date_ms, expected_date_ms, tz', day_start_date_ms_data)
def test_get_day_start_date_ms(date_ms, expected_date_ms, tz):
    assert TimeUtil.get_day_start_date_ms(date_ms, tz) == expected_date_ms


@pytest.mark.parametrize('timezone_str, expected_tz', timezone_date)
def test_get_timezone(timezone_str, expected_tz):
    assert TimeUtil.get_timezone(timezone_str) == expected_tz


def test_get_timezone_raise_exception_negative():
    with pytest.raises(ValueError):
        TimeUtil.get_timezone('Unknown')

    with pytest.raises(ValueError):
        TimeUtil.get_timezone('')

    with pytest.raises(ValueError):
        TimeUtil.get_timezone('UTC+1')


def test_get_timezone_offset_hours():
    assert TimeUtil.get_timezone_offset_hours('UTC') == 0
    assert 1 <= TimeUtil.get_timezone_offset_hours('Europe/Paris') <= 2
    assert -5 <= TimeUtil.get_timezone_offset_hours('America/New_York') <= -4
    assert 8 <= TimeUtil.get_timezone_offset_hours('Asia/Tokyo') <= 9
    assert 11 >= TimeUtil.get_timezone_offset_hours('Australia/Sydney') >= 10
    assert 10 >= TimeUtil.get_timezone_offset_hours('Australia/Adelaide') >= 9
    assert -8 <= TimeUtil.get_timezone_offset_hours('PDT') <= -7
    assert 2 <= TimeUtil.get_timezone_offset_hours('Asia/Jerusalem') <= 3
    assert 2 <= TimeUtil.get_timezone_offset_hours('Israel') <= 3


def test_get_timezone_offset_hours_negative():
    with pytest.raises(ValueError):
        TimeUtil.get_timezone_offset_hours('Unknown')

    with pytest.raises(ValueError):
        TimeUtil.get_timezone_offset_hours('')


def test_is_timeout_ms():
    start_time_ms = TimeUtil.get_current_date_ms()
    timeout_ms = 2000
    assert not TimeUtil.is_timeout_ms(start_time_ms, timeout_ms)
    sleep(3)
    assert TimeUtil.is_timeout_ms(start_time_ms, timeout_ms)


@pytest.mark.parametrize(
    'date_str, date_format, expected_result', is_date_in_format_data)
def test_is_date_in_format(date_str, date_format, expected_result):
    assert TimeUtil.is_date_in_format(date_str, date_format) == expected_result


@pytest.mark.parametrize('year, expected_result', is_leap_year_data)
def test_is_leap_year(year, expected_result):
    assert TimeUtil.is_leap_year(year) == expected_result
