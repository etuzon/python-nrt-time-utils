import datetime

import pytz
from datetime import timezone
from nrt_time_utils.time_utils import YMD_DATE_FORMAT, YMD_HMS_DATE_FORMAT, \
    YMD_HMSF_DATE_FORMAT, YMD_Z_DATE_FORMAT, YMD_HMS_Z_DATE_FORMAT, \
    YMD_HMSF_Z_DATE_FORMAT

date_str_to_date_ms_data = [
    ('2021-01-01 UTC', YMD_Z_DATE_FORMAT, 1609459200000),
    ('2021-01-01 02:00:00 UTC', YMD_HMS_Z_DATE_FORMAT, 1609466400000),
    ('2021-01-01 02:01:40 UTC', YMD_HMS_Z_DATE_FORMAT, 1609466500000),
    ('2021-01-01 02:02:00 UTC', YMD_HMS_Z_DATE_FORMAT, 1609466520000),
    ('UTC 2021-01-01 02:02:00', f'%Z {YMD_HMS_DATE_FORMAT}', 1609466520000),
    ('2021-01-01 02:02:00.000000 UTC', YMD_HMSF_Z_DATE_FORMAT, 1609466520000)
]


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


day_end_date_ms_data = [
    (1612137600000, 1612223999999, timezone.utc),
    (1612137600001, 1612223999999, 'UTC'),
    (1612137690000, 1612223999999, 'UTC'),
    (1612223999999, 1612223999999, 'UTC'),
    (0, 86399999, 'UTC'),
    (1612215799999, 1612216799999, 'Asia/Jerusalem')
]


day_start_date_ms_data = [
    (1612137600000, 1612137600000, timezone.utc),
    (1612137600001, 1612137600000, 'UTC'),
    (1612137690000, 1612137600000, 'UTC'),
    (1612137690000, 1612130400000, 'Asia/Jerusalem'),
    (0, 0, 'UTC')
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

timezone_date = [
    ('UTC', pytz.timezone('UTC')),
    ('GMT', pytz.timezone('GMT')),
    ('IST', pytz.timezone('Israel'))
]
