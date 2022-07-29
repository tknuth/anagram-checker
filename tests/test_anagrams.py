import pytest
import itertools as it
from anagram_checker import *

funcs = (
    tick_while,
    tick_for,
    sort,
    counter,
    collections_counter,
    prime_multiplication,
    brute_force,
)

anagram_tests = (
    ("lager", "regal", True),
    ("lagern", "regal", False),
    ("lager", "regale", False),
    ("silent", "listen", True),
    ("earth", "heart", True),
    ("lager", "nagel", False),
    ("biere", "reibe", True),
    ("auto", "fahrrad", False),
    ("mietshaus", "atheismus", True),
    ("lagerregal", "regallager", True),
    ("fahrplan", "planbar", False),
    ("auto", "auto", False),
)


@pytest.mark.parametrize("test_input", it.product(anagram_tests, funcs))
def test_anagram_checker(test_input):
    anagram_test, func = test_input
    a, b, is_anagram = anagram_test
    assert func(a, b) == is_anagram


def test_generate_primes():
    lst = []
    primes = generate_primes()
    lst = [next(primes) for prime in range(10)]
    assert lst == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_create_letter_dict():
    assert create_letter_dict() == {
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
        "f": 13,
        "g": 17,
        "h": 19,
        "i": 23,
        "j": 29,
        "k": 31,
        "l": 37,
        "m": 41,
        "n": 43,
        "o": 47,
        "p": 53,
        "q": 59,
        "r": 61,
        "s": 67,
        "t": 71,
        "u": 73,
        "v": 79,
        "w": 83,
        "x": 89,
        "y": 97,
        "z": 101,
    }
