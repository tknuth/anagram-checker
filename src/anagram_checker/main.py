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


def brute_force(a, b):
    # possible_words = []
    pass