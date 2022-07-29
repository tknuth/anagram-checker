from functools import wraps
import collections
import itertools as it
import string
from venv import create


def sanity_check(f):
    @wraps(f)
    def g(a, b):
        a = a.lower()
        b = b.lower()
        for w in (a, b):
            if not set(w) & set(string.ascii_lowercase) == set(w):
                raise Exception("invalid input")
        if len(a) != len(b):
            return False
        if a == b:
            return False
        return f(a, b)

    return g


def generate_primes():
    d = collections.defaultdict(list)
    i = 2
    while True:
        if i not in d:
            yield i
            d[i**2] = [i]
        else:
            for p in d[i]:
                d[p + i].append(p)
            del d[i]
        i += 1


def create_letter_dict():
    primes = generate_primes()
    return {letter: next(primes) for letter in string.ascii_lowercase}


@sanity_check
def prime_multiplication(a, b):
    d = create_letter_dict()
    na = 1
    nb = 1
    for letter in a:
        na *= d[letter]
    for letter in b:
        nb *= d[letter]
    return na == nb


@sanity_check
def tick_while(a, b):
    a = list(a)
    i = 0
    status = True
    while i < len(b) and status:
        j = 0
        found = False
        while j < len(a) and not found:
            if b[i] == a[j]:
                found = True
            else:
                j += 1
        if found:
            a[j] = None
        else:
            status = False
        i += 1

    return status


@sanity_check
def tick_for(a, b):
    a = list(a)
    for letter in b:
        for i in range(len(a)):
            if letter == a[i]:
                a[i] = None
                break

    for letter in a:
        if letter is not None:
            return False

    return True


@sanity_check
def sort(a, b):
    return sorted(a) == sorted(b)


@sanity_check
def collections_counter(a, b):
    a = collections.Counter(a)
    b = collections.Counter(b)
    return a == b


@sanity_check
def counter(a, b):
    p = {}
    q = {}
    for l, d in ((a, p), (b, q)):
        for letter in l:
            d[letter] = d.get(letter, 0) + 1
    return p == q


@sanity_check
def brute_force(a, b):
    permutations = list(it.permutations(a, len(a)))
    return tuple(b) in permutations
