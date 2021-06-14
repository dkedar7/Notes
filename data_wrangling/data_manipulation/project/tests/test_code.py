
import pytest

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from src.check_if_even import check_if_even

testdata = [
    (2, True),
    (3, False),
    (4, True),
    (5, True) # We expect this test to fail
    ]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_check_if_even(sample, expected_output):
    """
    Define test cases
    """

    assert check_if_even(sample) == expected_output
