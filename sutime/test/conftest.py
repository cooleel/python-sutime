from datetime import date, time, timedelta

import pytest


@pytest.fixture
def input_duration_range():
    return 'I need a desk for tomorrow from 2pm to 3pm'


@pytest.fixture
def input_christmas_eve():
    return 'christmas eve'


@pytest.fixture
def input_sunday_night():
    return 'Mary had spent Sunday night with us.'


@pytest.fixture
def input_duration():
    return 'I need a desk for tomorrow from 2pm for 2 hours'


@pytest.fixture
def input_today():
    return 'I have written a test today.'


@pytest.fixture(scope='module')
def tomorrow():
    return date.today() + timedelta(days=1)


@pytest.fixture(scope='module')
def two_pm():
    return time(hour=14)


@pytest.fixture(scope='module')
def three_pm():
    return time(hour=15)


@pytest.fixture(scope='module')
def reference_date():
    return date(2017, 1, 9)
