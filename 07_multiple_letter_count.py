def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counter = {}

    for char in phrase:
        if counter.get(char):
            counter[char] += 1
        else:
            counter[char] = 1

    return counter

    # More exciting attempts below:

    # CLOSE, but out of order??:

    # counter = {}
    # for char in set(phrase):
    #     counter[char] = phrase.count(char)

    # return counter

    # TypeError: 'builtin_function_or_method' object is not subscriptable

    # counter = {}
    # for char in phrase:
    #     if counter.get(char):
    #         continue
    #     else:
    #         counter[char] = phrase.count[char]
    # return counter
