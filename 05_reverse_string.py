def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    # This seems bad, so we refactored below
    # reversed_string = ""
    # for index in range(len(phrase)-1, -1, -1):
    #    reversed_string += phrase[index]
    # return reversed_string


    phrase = list(phrase)
    phrase.reverse()
    return "".join(phrase)