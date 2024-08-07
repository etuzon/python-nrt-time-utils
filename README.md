# Time Utilities

### Time utilities in Python.

![PyPI](https://img.shields.io/pypi/v/nrt-time-utils?color=blueviolet&style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nrt-time-utils?color=greens&style=plastic)
![PyPI - License](https://img.shields.io/pypi/l/nrt-time-utils?color=blue&style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dd/nrt-time-utils?style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dm/nrt-time-utils?color=yellow&style=plastic)
[![Coverage Status](https://coveralls.io/repos/github/etuzon/python-nrt-time-utils/badge.svg)](https://coveralls.io/github/etuzon/python-nrt-time-utils)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/etuzon/python-nrt-time-utils?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/etuzon/python-nrt-time-utils?style=plastic)
[![DeepSource](https://app.deepsource.com/gh/etuzon/python-nrt-time-utils.svg/?label=active+issues&show_trend=false&token=eTDGJ29l60LGTuhQtl6DQqJG)](https://app.deepsource.com/gh/etuzon/python-nrt-time-utils/)

## TimeUtil class

### Methods

| **Method**                  | **Description**                                        | **Parameters**                                                                                                                                                                                          | **Returns**                                                        |
|-----------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| `date_ms_to_date_str`       | Converts a date in milliseconds to a date string.      | `date_ms (int)` The date in milliseconds to convert to a date string.<br>`date_format (str, Default: YMD_HMSF_DATE_FORMAT)` The format string to convert the date to.<br>`tz (Default: None)` Timezone. | `str` The date string.                                             |
| `date_ms_to_date_time`      | Converts a date in milliseconds to a date time object. | `date_ms (int)` The date in milliseconds to convert to a date time object.<br>`tz (Default: None)` Timezone.                                                                                            | `datetime` The date time object.                                   |
| `date_str_to_date_ms`       | Converts a date string to a date in milliseconds.      | `date_str (str)` The date string to convert to a date in milliseconds.<br>`date_format (str, Default: YMD_HMSF_DATE_FORMAT)` The format string to convert the date to.                                  | `int` The date in milliseconds.                                    |
| `date_str_to_date_time`     | Converts a date string to a date time object.          | `date_str (str)` The date string to convert to a date time object.<br>`date_format (str, Default: YMD_HMSF_DATE_FORMAT)` The format string to convert the date to.                                      | `datetime` The date time object.                                   |
| `date_time_to_date_ms`      | Converts a date time object to a date in milliseconds. | `dt (datetime)` The date time object to convert to a date in milliseconds.                                                                                                                              | `int` The date in milliseconds.                                    |
| `get_current_date_ms`       | Returns the current date in milliseconds.              |                                                                                                                                                                                                         | `int` The current date in milliseconds.                            |
| `get_day_end_date_ms`       | Returns the end of the day in milliseconds.            | `date_ms (int)` The date in milliseconds to get the end of the day.<br>`tz (Default: None)` Timezone.                                                                                                   | `int` The end of the day in milliseconds.                          |
| `get_day_start_date_ms`     | Returns the start of the day in milliseconds.          | `date_ms (int)` The date in milliseconds to get the start of the day.<br>`tz (Default: None)` Timezone.                                                                                                 | `int` The start of the day in milliseconds.                        |
| `get_timezone`              | Returns the timezone.                                  | `timezone_str (str)` A string representing the timezone.                                                                                                                                                | pytz timezone.<br>Raise Value error in case the timezone not exist |
| `get_timezone_offset_hours` | Returns the timezone offset in hours.                  | `timezone_str (str)` A string representing the timezone.                                                                                                                                                | `int` The timezone offset in hours.                                |
| `is_leap_year`              | Checks if a year is a leap year.                       | `year (int)` The year to check if it is a leap year.                                                                                                                                                    | `bool` True if the year is a leap year, False otherwise.           |
| `is_timeout_ms`             | Checks if a timeout in milliseconds has passed.        | `start_time_ms (int)` The start time in milliseconds.<br>`timeout_ms (int)` The timeout in milliseconds.                                                                                                | `bool` True if the timeout has passed, False otherwise.            |
| `is_date_in_format`         | Checks if a date string is in a specific format.       | `date_str (str)` The date string to check.<br>`format_str (str)` The format string to check.                                                                                                            | `bool` True if the date string is in the format, False otherwise.  |

### Examples:

- #### TimeUtil.date_ms_to_date_str

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil

    # Convert a date in milliseconds to a date string
    date_str = TimeUtil.date_ms_to_date_str(1617223200000)

    print(date_str)
    ```
    **Output**
    ```
    2021-03-31 00:00:00.000
    ```

- #### TimeUtil.date_ms_to_date_time
        
    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil

    # Convert a date in milliseconds to a date time object
    dt = TimeUtil.date_ms_to_date_time(1609459200000, 'UTC')

    print(dt)
  
    dt = TimeUtil.date_ms_to_date_time()
    ```
    **Output**
    ```
    2021-01-01 00:00:00+00:00
    ```

- #### TimeUtil.date_str_to_date_ms
     
    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil, YMD_HMSF_Z_DATE_FORMAT

    # Convert a date string to a date in milliseconds
    date_ms = \
        TimeUtil.date_str_to_date_ms(
            '2021-01-01 02:02:00.000000 UTC', YMD_HMSF_Z_DATE_FORMAT)

    print(date_ms)
    ```
    **Output**
    ```
    1609466520000
    ```
  
- #### TimeUtil.date_str_to_date_time

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil

    # Convert a date string to a date time object
    dt = TimeUtil.date_str_to_date_time('2021-03-31 00:00:00.000')

    print(dt)
    ```
    **Output**
    ```
    2021-03-31 00:00:00
    ```

- #### TimeUtil.date_time_to_date_ms

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil
    from datetime import datetime

    # Convert a date time object to a date in milliseconds
    date_ms = TimeUtil.date_time_to_date_ms(datetime(2021, 3, 31, 0, 0, 0))

    print(date_ms)
    ```
    **Output**
    ```
    1617223200000
    ```
  
- #### TimeUtil.get_current_date_ms

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil

    # Get the current date in milliseconds
    current_date_ms = TimeUtil.get_current_date_ms()

    print(current_date_ms)
    ```
    **Output**
    ```
    1617223200000
    ```

- #### TimeUtil.get_day_end_date_ms

   **Code**
   ```python
   from nrt_time_utils.time_utils import TimeUtil
  
   # Get the end of the day in milliseconds
   day_end_date_ms = TimeUtil.get_day_end_date_ms(1612137600001, 'UTC')
  
   print(day_end_date_ms)
   ```
   **Output** 
   ```
   1612223999999
   ```

- #### TimeUtil.get_day_start_date_ms

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil

    # Get the start of the day in milliseconds
    day_start_date_ms = TimeUtil.get_day_start_date_ms(1612137600001, 'UTC')

    print(day_start_date_ms)
    ```
    **Output**
    ```
    1612137600000
    ```

- #### TimeUtil.get_timezone
    
    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil

    # Get the timezone
    timezone = TimeUtil.get_timezone('Asia/Jerusalem')

    print(timezone)
    ```
    **Output**
    ```
    Asia/Jerusalem
    ```

- #### TimeUtil.get_timezone_offset_hours

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil

    # Get the timezone offset in hours
    timezone_offset = TimeUtil.get_timezone_offset_hours('PDT')

    print(timezone_offset)
    ```
    **Output**
    ```
    -7
    ```

- #### TimeUtil.is_leap_year

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil

    # Check if a year is a leap year
    is_leap_year = TimeUtil.is_leap_year(2020)

    print(is_leap_year)
    ```
    **Output**
    ```
    True
    ```
  
- #### TimeUtil.is_timeout_ms

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil
    from time import sleep

    current_date_ms = TimeUtil.get_current_date_ms()
    is_timeout = TimeUtil.is_timeout_ms(current_date_ms, 1000)
    print(is_timeout)
    sleep(2)
    is_timeout = TimeUtil.is_timeout_ms(current_date_ms, 1000)
    print(is_timeout)
    ```
    **Output**
    ```
    False
    True
    ```
  
- #### TimeUtil.is_date_in_format

    **Code**
    ```python
    from nrt_time_utils.time_utils import TimeUtil, YMD_HMSF_DATE_FORMAT

    # Check if a date string is in a specific format
    is_date_in_format = \
        TimeUtil.is_date_in_format('2021-03-31 00:00:00.000', YMD_HMSF_DATE_FORMAT)

    print(is_date_in_format)
    ```
    **Output**
    ```
    True
    ```
  
## Timer methods

Record the time it takes to execute a method or a block of code.

### Methods

| **Method**                | **Description**                                                                                                                                    | **Parameters**                                                                                                               | **Returns**                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| `method_timer`            | Measure method execution time.                                                                                                                     | `function` The method to measure it's time.<br>`*args` The method's arguments.<br>`**kwargs` The method's keyword arguments. | `Timer` Object that contains method execution time and results.                  |
| `timer` decorator         | Timer decorator that measure the method execution time, and add the results to parameter, that can be accessed by the method `get_timer_results()` | `is_enabled (bool, Default: True)` If True, the timer is enabled, otherwise it is disabled.                                  | `any` Method result.                                                             |
| `get_timer_results`       | Returns the timer results.                                                                                                                         |                                                                                                                              | `dict[list[Timer]]` The timer results.<br>`{'FILE_PATH:Class.Method: [Timer]}'`. |
| `reset_timer_results`     | Resets the timer results.                                                                                                                          |                                                                                                                              |                                                                                  |
| `get_max_keys`            | Returns the maximum amount of allowed keys in the timer results.                                                                                   |                                                                                                                              | `int` The maximum amount of allowed keys in the timer results.                   |
| `set_max_keys`            | Sets the maximum amount of allowed keys in the timer results.                                                                                      | `max_keys (int)` The maximum amount of allowed keys in the timer results.                                                    |                                                                                  |
| `get_max_results_per_key` | Returns the maximum amount of allowed results per key in the timer results.                                                                        |                                                                                                                              | `int` The maximum amount of allowed results per key in the timer results.        |
| `set_max_results_per_key` | Sets the maximum amount of allowed results per key in the timer results.                                                                           | `max_results_per_key (int)` The maximum amount of allowed results per key in the timer results.                              |                                                                                  |
| `with Timer() as t:`      | Context manager that times a block of code.                                                                                                        |                                                                                                                              | `Timer` Object that contains block execution time and results.                   |

### Timer class

| **Parameters**             | **Description**                                                             | **Type**    | **Default** |
|----------------------------|-----------------------------------------------------------------------------|-------------|-------------|
| `start_date_ms`            | The start date in milliseconds.                                             | `int`       |             |
| `end_date_ms`              | The end date in milliseconds.                                               | `int`       | `None`      |
| `execution_time_ms`        | The execution time in milliseconds.                                         | `int`       | `None`      |
| `result`                   | The result of the method.                                                   | `any`       | `None`      |
| `exception`                | The exception that occurred during the method execution.                    | `Exception` | `None`      |
| `stack_trace`              | The stack trace of the exception that occurred during the method execution. | `str`       | `None`      |
| `__enter__` and `__exit__` | Context manager methods (`with Timer() as t:`).                             |             |             |

### Examples:

- #### method_timer

    **Code**
    ```python
    from from nrt_time_utils.timer import method_timer

    def my_method(a, b):
        return a + b

    timer = method_timer(my_method, 1, 2)

    print(timer.execution_time_ms)
    ```

    **Output**
    ```
    1
    ```
  
- #### timer decorator

    **Code**
    ```python
    from time import sleep  
    from from nrt_time_utils.timer import timer, get_timer_results

    @timer()
    def my_method(a, b):
        sleep(1)
        return a + b

    my_method(1, 2)
  
    timer_results = get_timer_results()
  
    for timer_result_list in timer_results.values():
        print(timer_result_list[0].execution_time_ms)
    ```

    **Output**
    ```
    1001
    ```
  
- #### with Timer() as t:
    
    **Code**
    ```python
    from time import sleep
    from from nrt_time_utils.timer import Timer

    with Timer() as t:
        sleep(1)
  
    print(t.execution_time_ms)
    ```

    **Output**
    ```
    1000
    ```
