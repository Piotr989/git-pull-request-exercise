from example import apply, calculate_func_on_interval, response_on_ultimate_question

import numpy.testing as npt


def test_response_on_ultimate_question():
    """Test the response to the ultimate question of life, the universe, and everything."""
    assert response_on_ultimate_question() == 42


def test_apply():
    """Test the apply function with a simple lambda function."""
    result = apply(lambda x: x + 1, [1, 2, 3])
    npt.assert_array_equal(result, [2, 3, 4])


def test_calculate_func_on_interval():
    """Test the calculate_func_on_interval function with a simple lambda function."""
    result = calculate_func_on_interval(lambda x: x**2, 0, 20, num_points=5)
    expected = [0, 25, 100, 225, 400]
    npt.assert_array_almost_equal(result, expected)
