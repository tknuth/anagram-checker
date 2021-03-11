import collections
import itertools as it


def tick_while(a, b):
    if len(a) != len(b):
        return False

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


def tick_for(a, b):
    if len(a) != len(b):
        return False

    a = list(a)
    for letter in b:
        for i in range(len(a)):
            if letter == a[i]:
                a[i] = None

    for letter in a:
        if letter is not None:
            return False

    return True


def sort(a, b):
    return sorted(a) == sorted(b)


def collections_counter(a, b):
    a = collections.Counter(a)
    b = collections.Counter(b)
    return a == b


def counter(a, b):
    p = {}
    q = {}
    for l, d in ((a, p), (b, q)):
        for letter in l:
            d[letter] = d.get(letter, 0) + 1
    return p == q


def brute_force(a, b):
    permutations = list(it.permutations(a, len(a)))
    return tuple(b) in permutations
