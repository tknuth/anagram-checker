from anagram_checker import tick_while, tick_for, brute_force
import pytest

tuples = (
    ("lager", "regal", True),
    ("lagern", "regal", False),
    ("lager", "regale", False),
    ("lager", "nagel", False),
    ("biere", "reibe", True),
)


@pytest.mark.parametrize("tuple", tuples)
def test_tick_while(tuple):
    a, b, is_anagram = tuple
    assert tick_while(a, b) == is_anagram


@pytest.mark.parametrize("tuple", tuples)
def test_tick_for(tuple):
    a, b, is_anagram = tuple
    assert tick_for(a, b) == is_anagram


@pytest.mark.parametrize("tuple", tuples)
def test_brute_force(tuple):
    a, b, is_anagram = tuple
    # assert brute_force(a, b) == is_anagram