import pytest
from time import sleep

from nrt_time_utils.time_utils import SECOND_MS
from nrt_time_utils.timer import timer, reset_timer_results, get_timer_results, \
    get_max_keys, set_max_keys, get_max_results_per_key, set_max_results_per_key, \
    method_timer, Timer


class TimerTest:

    @timer()
    def func_timer_decorator_sleep_1_sec(self, return_value: int):
        sleep(1)
        return return_value


@timer()
def func_timer_decorator_sleep_1_sec(return_value: int):
    sleep(1)
    return return_value


@timer(is_enabled=False)
def func_timer_decorator_sleep_1_sec_disabled(return_value: int):
    sleep(1)
    return return_value


@timer()
def func_timer_decorator_sleep_2_sec(return_value: int):
    sleep(2)
    return return_value


@timer()
def func_timer_decorator_raise_exception():
    sleep(1)
    raise ValueError('Test exception')


def func_timer_sleep_1_sec(return_value: int):
    sleep(1)
    return return_value


@pytest.fixture(scope='function')
def setup_before_test():
    reset_timer_results()


def test_method_timer_decorator(setup_before_test):
    r_1 = func_timer_decorator_sleep_1_sec(1)
    r_2 = func_timer_decorator_sleep_1_sec(2)
    r_3 = func_timer_decorator_sleep_1_sec(3)

    __verify_method_decorator_results(r_1, r_2, r_3, get_timer_results())


def test_method_timer_decorator_in_class(setup_before_test):
    timer_test = TimerTest()

    r_1 = timer_test.func_timer_decorator_sleep_1_sec(1)
    r_2 = timer_test.func_timer_decorator_sleep_1_sec(2)
    r_3 = timer_test.func_timer_decorator_sleep_1_sec(3)

    __verify_method_decorator_results(r_1, r_2, r_3, get_timer_results())


def test_method_timer_decorator_raise_exception(setup_before_test):
    try:
        func_timer_decorator_raise_exception()
    except ValueError:
        pass

    timer_results = get_timer_results()

    assert len(timer_results) == 1

    key = list(timer_results.keys())[0]

    assert len(timer_results[key]) == 1

    timer_result = timer_results[key][0]

    assert timer_result.result is None
    assert isinstance(timer_result.exception, ValueError)
    assert timer_result.stack_trace is not None
    __verify_timer_result_of_sleep_1_sec(timer_result)


def test_max_keys(setup_before_test):
    original_max_keys = get_max_keys()

    try:
        set_max_keys(1)
        assert get_max_keys() == 1
        r_1 = func_timer_decorator_sleep_1_sec(1)
        _ = func_timer_decorator_sleep_2_sec(2)
        timer_results = get_timer_results()
        assert r_1 == 1
        assert len(timer_results) == 1
        key = list(timer_results.keys())[0]
        assert 'func_timer_decorator_sleep_1_sec' in key

    finally:
        set_max_keys(original_max_keys)
        assert get_max_keys() == original_max_keys


def test_max_results_per_key(setup_before_test):
    original_max_results_key = get_max_results_per_key()

    try:
        set_max_results_per_key(1)
        assert get_max_results_per_key() == 1
        r_1 = func_timer_decorator_sleep_1_sec(1)
        r_2 = func_timer_decorator_sleep_1_sec(2)

        assert r_1 == 1
        assert r_2 == 2

        timer_results = get_timer_results()

        assert len(timer_results) == 1

        key = list(timer_results.keys())[0]

        assert 'func_timer_decorator_sleep_1_sec' in key
        assert len(timer_results[key]) == 1
        assert timer_results[key][0].result == 2

    finally:
        set_max_results_per_key(original_max_results_key)
        assert get_max_results_per_key() == original_max_results_key


def test_timer_decorator_disabled(setup_before_test):
    r_1 = func_timer_decorator_sleep_1_sec(1)
    r_2 = func_timer_decorator_sleep_1_sec_disabled(2)
    r_3 = func_timer_decorator_sleep_1_sec_disabled(3)

    assert r_1 == 1
    assert r_2 == 2
    assert r_3 == 3

    timer_results = get_timer_results()

    assert len(timer_results) == 1

    key = list(timer_results.keys())[0]
    assert len(timer_results[key]) == 1
    assert timer_results[key][0].result == 1
    assert timer_results[key][0].exception is None
    assert timer_results[key][0].stack_trace is None


def test_method_timer(setup_before_test):
    timer_result = method_timer(func_timer_sleep_1_sec, 1)

    assert timer_result.result == 1
    assert timer_result.exception is None
    assert timer_result.stack_trace is None
    assert len(get_timer_results()) == 0


def test_with_block(setup_before_test):
    with Timer() as t:
        assert t.end_date_ms is None
        assert t.execution_time_ms is None
        sleep(1)

    assert t.result is None
    assert t.exception is None
    assert t.stack_trace is None
    assert t.execution_time_ms >= SECOND_MS
    assert t.execution_time_ms <= 2 * SECOND_MS
    assert t.start_date_ms > 0
    assert t.start_date_ms < t.end_date_ms

    time_str = str(t)
    assert 'Start date ms' in time_str
    assert 'End date ms' in time_str
    assert 'Execution time ms' in time_str


def test_with_block_raise_exception(setup_before_test):
    try:
        with Timer() as t:
            sleep(1)
            raise ValueError('Test exception')
    except ValueError:
        pass

    assert t.result is None
    assert isinstance(t.exception, ValueError)
    assert t.stack_trace is not None
    assert t.execution_time_ms >= SECOND_MS
    assert t.execution_time_ms <= 2 * SECOND_MS
    assert t.start_date_ms > 0
    assert t.start_date_ms < t.end_date_ms


def __verify_timer_result_of_sleep_1_sec(timer_result):
    assert timer_result.execution_time_ms >= SECOND_MS
    assert timer_result.execution_time_ms <= 2 * SECOND_MS
    assert timer_result.start_date_ms > 0
    assert timer_result.start_date_ms < timer_result.end_date_ms


def __verify_method_decorator_results(r_1, r_2, r_3, timer_results: dict):
    assert r_1 == 1
    assert r_2 == 2
    assert r_3 == 3

    assert len(timer_results) == 1

    key = list(timer_results.keys())[0]

    assert len(timer_results[key]) == 3

    for timer_result in timer_results[key]:
        assert timer_result.result in [1, 2, 3]
        assert timer_result.exception is None
        assert timer_result.stack_trace is None
        __verify_timer_result_of_sleep_1_sec(timer_result)
