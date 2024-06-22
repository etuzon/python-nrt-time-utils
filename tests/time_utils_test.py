from time import sleep

import pytest

from nrt_time_utils.time_utils import TimeUtil, YMD_HMS_DATE_FORMAT, YMD_HMSF_DATE_FORMAT
from tests.time_utils_data import \
    date_str_to_date_time_data, is_date_in_format_data, is_leap_year_data


def test_date_ms_to_date_str():
    date_str = TimeUtil.date_ms_to_date_str(1609459200000, YMD_HMSF_DATE_FORMAT)
    assert date_str is not None


def test_date_ms_to_date_time():
    date_time = TimeUtil.date_ms_to_date_time(1609459200000)
    assert date_time


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


def test_get_timezone_offset_hours():
    assert TimeUtil.get_timezone_offset_hours('UTC') == 0
    assert TimeUtil.get_timezone_offset_hours('Europe/Paris') == 2
    assert TimeUtil.get_timezone_offset_hours('America/New_York') == -4
    assert TimeUtil.get_timezone_offset_hours('Asia/Tokyo') == 9
    assert TimeUtil.get_timezone_offset_hours('Australia/Sydney') == 10
    assert TimeUtil.get_timezone_offset_hours('Australia/Adelaide') == 9
    assert TimeUtil.get_timezone_offset_hours('PDT') == -7
    assert TimeUtil.get_timezone_offset_hours('Asia/Jerusalem') == 3
    assert TimeUtil.get_timezone_offset_hours('Israel') == 3


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
