
import pytest

testdata = [
    (2, True),
    (3, False),
    (4, True),
    (5, True) # We expect this test to fail
    ]

def check_if_even(a):
    """
    Returns True if 'a' is an even number
    """
    return a % 2 == 0

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_check_if_even(sample, expected_output):
    """
    Define test cases
    """

    assert check_if_even(sample) == expected_output
