import pytest
import itertools as it
from anagram_checker import *

funcs = (
    tick_while,
    tick_for,
    sort,
    counter,
    collections_counter,
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
)


@pytest.mark.parametrize("test_input", it.product(anagram_tests, funcs))
def test_anagram_checker(test_input):
    anagram_test, func = test_input
    a, b, is_anagram = anagram_test
    assert func(a, b) == is_anagram