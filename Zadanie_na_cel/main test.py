import pytest
from typing import List, Tuple

# Import the solution function
from main import max_scores

def test_example_1():
    nums = [10, 15, 2, 7]
    expected = (22, 12)  # The expected output given in the problem
    assert max_scores(nums) == expected

def test_example_2():
    nums = [7,3,10,15,2,6]
    expected = (25,18)  # The expected output given in the problem
    assert max_scores(nums) == expected


def test_example_3():
    nums = [3, 9, 1, 2]
    expected = (11, 4)  # The expected output given in the problem
    assert max_scores(nums) == expected

def test_single_element():
    nums = [42]
    expected = (42, 0)  # Player 1 gets the only number
    assert max_scores(nums) == expected

def test_two_elements():
    nums = [5, 8]
    expected = (8, 5)  # Player 1 picks 8, player 2 gets 5
    assert max_scores(nums) == expected

def test_all_same_values():
    nums = [3, 3, 3, 3]
    # Both players get equal sums if values are the same and length is even
    expected = (6, 6)
    assert max_scores(nums) == expected

def test_decreasing_sequence():
    nums = [10, 9, 8, 7, 6]
    # Optimal play would be P1: 10, P2: 9, P1: 8, P2: 7, P1: 6
    expected = (24, 16)
    assert max_scores(nums) == expected

def test_increasing_sequence():
    nums = [1, 2, 3, 4, 5]
    # Optimal play would be P1: 5, P2: 4, P1: 3, P2: 2, P1: 1
    expected = (9, 6)
    assert max_scores(nums) == expected

def test_large_input():
    # Creating a larger input to test performance
    nums = list(range(1, 101))  # 100 elements
    # Without running the full calculation, we can't determine the expected result
    # But we can ensure the function runs without error and returns a tuple of two ints
    result = max_scores(nums)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int) and isinstance(result[1], int)
    assert result[0] + result[1] == sum(nums)  # Sum of scores should equal sum of nums