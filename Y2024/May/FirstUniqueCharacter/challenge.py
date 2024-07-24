from collections import defaultdict


def first_unique_character(s):
    counter = defaultdict(int)
    for chars in s:
        counter[chars] += 1

    for char, count in counter.items():
        if count == 1:
            return s.index(char)
    else:
        return -1
