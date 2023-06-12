import pytest

import pklearn


@pytest.fixture
def print_changed_only_false():
    pklearn.set_config(print_changed_only=False)
    yield
    pklearn.set_config(print_changed_only=True)  # reset to default
