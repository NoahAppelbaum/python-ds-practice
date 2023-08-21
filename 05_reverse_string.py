def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_string = ""
    for index in range(len(phrase)-1, -1, -1):
        reversed_string += phrase[index]
    return reversed_string

# FIXME: This seems bad.
