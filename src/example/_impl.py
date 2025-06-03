from typing import Callable, Iterable, List, TypeVar

T = TypeVar('T')
V = TypeVar('V')

def response_on_ultimate_question():
    """
    This function returns a response to the ultimate question of life, the universe, and everything.
    """
    return 42


def calculate_func_on_interval(
    func: Callable[[float], T], start: float, end: float, num_points: int=100
) -> List[T]:
    """This function calculates the sum of a function evaluated at discrete points in a given interval.
    """
    diff = end - start
    step = diff / num_points
    return [func(start + i * step) for i in range(num_points)]


def apply(func: Callable[[T], V], iterable: Iterable[T]) -> List[V]:
    """This function applies a given function to each element in an iterable and returns a list of results.
    """
    return [func(x) for x in iterable]