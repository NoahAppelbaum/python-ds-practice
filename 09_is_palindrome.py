def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.lower()

    start = 0
    end = len(phrase) - 1

    while start < end:
        if phrase[start] == " ":
            start += 1
        elif phrase[end] == " ":
            end -= 1
        elif phrase[start] == phrase[end]:
            start += 1
            end -= 1
        else:
            return False

    return True
