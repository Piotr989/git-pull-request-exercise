from typing import Callable, Iterable, List, TypeVar
import numpy as np

T = TypeVar('T')
V = TypeVar('V')

def response_on_ultimate_question() -> int:
    """
    This function returns a response to the ultimate question of life, the universe, and everything.
    """
    return 42


def calculate_func_on_interval(
    func: Callable[[float], T],
    start: float,
    end: float,
    num_points: int=100
) -> List[T]:
    """This function calculates the sum of a function evaluated at discrete points in a given interval.

    Parameters
    ----------
    func : Callable[[float], T]
        The function to be evaluated.
    start : float
        The starting point of the interval.
    end : float
        The ending point of the interval.
    num_points : int, optional
        The number of points at which to evaluate the function, by default 100.

    Returns
    -------
    List[T]
        A list containing the results of the function evaluated at each point in the interval.
    """
    return [func(v) for v in np.linspace(start, end, num_points)]


def apply(
    func: Callable[[T], V],
    iterable: Iterable[T]
) -> List[V]:
    """This function applies a given function to each element in an iterable and returns a list of results.

    Parameters
    ----------
    func : Callable[[T], V]
        The function to be applied to each element.
    iterable : Iterable[T]
        The iterable containing elements to which the function will be applied.

    Returns
    -------
    List[V]
        A list containing the results of applying the function to each element in the iterable.
    """
    return [func(x) for x in iterable]