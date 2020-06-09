from functools import lru_cache
from typing import Tuple
import pytest


# Fibonacci
# -------------------------------------------------------------------------------------
@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """
    :param n: n'th number in Fibonacci sequence, starts from 1
    :return: n'th number value in Fibonacci sequence
    """
    if 1 == n or n == 2:
        return 1
    elif n > 2 and isinstance(n, int):
        return fibonacci(n - 1) + fibonacci(n - 2)
    return -1


@lru_cache(maxsize=None)
def fibonacci_iter(n: int) -> Tuple:
    """
    :param n: n'th number in Fibonacci sequence, starts from 1
    :return: Fibonacci sequence from 1 to n
    """
    if n == 1:
        return (1,)
    elif n > 1:
        return fibonacci_iter(n - 1) + (fibonacci(n),)
    return (-1,)


print('Fibonacci check: {}'.format(fibonacci_iter(6) == (1, 1, 2, 3, 5, 8)))  # True


def test_fib_input():
    assert fibonacci(-4) == -1


def test_fib_logic():
    assert fibonacci(6) == 8


def test_fib_calls():
    _ = fibonacci(6)
    assert fibonacci.cache_info()[1] == 7


class BasePizza:
    def __init__(self, dough=100, tomato_paste=50):
        self.name = self.__class__.__name__
        self.dough = dough
        self.tomato_paste = tomato_paste

    def dict(self):
        return {'dough': self.dough, 'tomato_paste': self.tomato_paste}

    def __repr__(self):
        recipe = self.name + ': '
        for ingredient, gram in self.dict().items():
            recipe += ingredient + ' ' + str(gram) + ' g., '

        return recipe


class Margherita(BasePizza):

    def __init__(self, cheese):
        super().__init__()
        self.cheese = cheese

    def dict(self):
        parent_args = super().dict()
        parent_args.update({'cheese': self.cheese})
        return parent_args


class Pepperoni(BasePizza):

    def __init__(self, pepperoni):
        super().__init__()
        self.pepperoni = pepperoni

    def dict(self):
        parent_args = super().dict()
        parent_args.update({'pepperoni': self.pepperoni})
        return parent_args


class Hawaiian(BasePizza):
    chicken = True
    pineapple = True

    def __init__(self, chicken, pineapple):
        super().__init__()
        self.chicken = chicken
        self.pineapple = pineapple

    def dict(self):
        parent_args = super().dict()
        parent_args.update({'chicken': self.chicken, 'pineapple': self.pineapple})
        return parent_args


print('Pizzas name check: {}, pizza method check {}'.format(Hawaiian(10, 20), Hawaiian(10, 20).dict()))

# -------------------------------------------------------------------------------------


# Logger
# -------------------------------------------------------------------------------------
from functools import wraps
from time import sleep
from datetime import datetime
import logging


def time_log(prefix=''):
    """
    Counts time and adds prefix
    """

    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            logging.basicConfig(filename='example.txt', filemode='a+', level=logging.DEBUG)
            logging.debug('Start: {}'.format(datetime.now()))
            result = func(*args, **kwargs)
            logging.debug('End: {}'.format(datetime.now()))
            return result

        return inner_wrapper

    return outer_wrapper


@time_log('logged ')
def dummy_func():
    return sleep(3)


dummy_func()
