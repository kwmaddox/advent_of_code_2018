import pytest
from day1 import part1,part2
from unittest import mock
import decorators

@pytest.mark.parametrize("test_input, expected",
                         [("+1\n+1\n+1\n", 3),
                         ("+1\n+1\n-2\n", 0),
                         ("-1\n-2\n-3\n", -6)])
@decorators.patch_io("test_input")
def test_part1_from_problem_def(test_input, expected):
    # with mock.patch("decorators.open", mock.mock_open(read_data=test_input)) as mock_file:
    assert part1() == expected
    # assert_false

@pytest.mark.parametrize("test_input, expected",
                         [("+1\n-1", 0),
                         ("+3\n+3\n+4\n-2\n-4\n", 10),
                         ("-6\n+3\n+8\n+5\n-6", 5),
                         ("+7\n+7\n-2\n-7\n-4", 14)])
@decorators.patch_io("test_input")
def test_part2_from_problem_def(test_input, expected):
    # with mock.patch("decorators.open", mock.mock_open(read_data=test_input)) as mock_file:
    assert part2() == expected