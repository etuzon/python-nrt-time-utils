import datetime

from nrt_time_utils.time_utils import YMD_DATE_FORMAT, YMD_HMS_DATE_FORMAT, \
    YMD_HMSF_DATE_FORMAT


date_str_to_date_time_data = [
    ('2021-01-01', YMD_DATE_FORMAT,
     datetime.datetime(2021, 1, 1, 0, 0, 0, 0, None)),
    ('2021-01-01 02:00:00', YMD_HMS_DATE_FORMAT,
     datetime.datetime(2021, 1, 1, 2, 0, 0, 0, None)),
    ('2021-01-01 02:01:40', YMD_HMS_DATE_FORMAT,
     datetime.datetime(2021, 1, 1, 2, 1, 40, 0, None)),
    ('2021-01-01 02:02:00', YMD_HMS_DATE_FORMAT,
     datetime.datetime(2021, 1, 1, 2, 2, 0, 0, None)),
    ('2021-01-01 02:02:00.040000', YMD_HMSF_DATE_FORMAT,
     datetime.datetime(2021, 1, 1, 2, 2, 0, 40000, None)),
]


is_date_in_format_data = [
    ('2021-01-01', YMD_DATE_FORMAT, True),
    ('2021-01-01 02:00:00', YMD_HMS_DATE_FORMAT, True),
    ('2021-01-01 02:01:40', YMD_HMS_DATE_FORMAT, True),
    ('2021-01-01 02:02:00', YMD_HMS_DATE_FORMAT, True),
    ('2021-01-01 02:02:00.040000', YMD_HMSF_DATE_FORMAT, True),
    ('2021-01-01 02:02:00.045000', YMD_HMSF_DATE_FORMAT, True),
    ('2021-01-01 02:02:00.045000', YMD_HMS_DATE_FORMAT, False),
    ('2021-01-01 02:02:00.045000', YMD_DATE_FORMAT, False),
    ('2021-01-01 02:02:00', YMD_HMSF_DATE_FORMAT, False),
    ('2021-01-01 02:02:00.040000', YMD_HMS_DATE_FORMAT, False),
    ('2021-01-01 02:02:00.040000', YMD_DATE_FORMAT, False),
    ('2021-01-01 02:02:00.045000', YMD_HMS_DATE_FORMAT, False),
    ('2021-01-01 02:02:00.045000', YMD_DATE_FORMAT, False),
]

is_leap_year_data = [
    (1900, False),
    (2000, True),
    (2020, True),
    (2021, False),
    (2022, False),
    (2023, False),
    (2024, True),
    (2100, False),
    (2400, True)
]
