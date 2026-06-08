# Tests — DSA-Arrays-Mastery
# Run: pytest tests/ -v

import pytest

def test_kadane():
    assert kadane([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert kadane([-1,-2,-3]) == -1          # all negative
    assert kadane([5]) == 5                   # single element
    assert kadane([1,2,3,4,5]) == 15          # all positive

def test_rotate():
    assert rotate_array([1,2,3,4,5,6,7],3) == [5,6,7,1,2,3,4]
    assert rotate_array([1,2],3) == [2,1]     # k > n

def test_subarray_sum():
    assert subarray_sum_k([1,1,1],2) == 2
    assert subarray_sum_k([1,2,3],3) == 2
    assert subarray_sum_k([1],0) == 0

def test_rain_water():
    assert trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_rain_water([4,2,0,3,2,5]) == 9
    assert trap_rain_water([]) == 0 if not [] else True