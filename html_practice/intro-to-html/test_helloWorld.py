# def test_func():
#     #computes 2+2
#     assert 2+2 == 4

# import pytest
import time

def time_consuming_function():
    # Simulate a time-consuming task
    time.sleep(2)

def test_performance():
    start_time = time.time()
    time_consuming_function()
    execution_time = time.time() - start_time

    # Assert that the execution time is within the expected range
    assert execution_time < 3  # Assuming the expected execution time is less than 3 seconds