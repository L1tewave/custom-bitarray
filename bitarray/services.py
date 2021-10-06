"""
Useful functions
"""
from bitarray.settings import STR_ZERO_AND_ONE, CHAR_LENGTH, LIST_ZERO_AND_ONE


def is_char_0_or_1(char: str) -> bool:
    """
    Checks if the character passed in is a string zero or one

    Parameters
    ----------
    char : str
        line of length 1

    Returns
    -------
    bool
        True or False

    Raises
    ------
    ValueError
        when a string with length greater than 1 is transmitted

    Examples
    --------
    >>> is_char_0_or_1("0")
    True
    >>> is_char_0_or_1("2")
    False
    """
    if len(char) != CHAR_LENGTH:
        raise ValueError("Function must be called for single characters")
    return char in STR_ZERO_AND_ONE


def is_bool(item) -> bool:
    """
    Checks if the passed object belongs to a boolean type

    Parameters
    ----------
    item : Any
        some object

    Returns
    -------
    bool
        True or False

    Examples
    --------
    >>> is_bool(0)
    False
    >>> is_bool(False)
    True
    """
    return isinstance(item, bool)


def is_int_0_or_1(item) -> bool:
    """
    Checks if the character passed in is a int zero or one

    Parameters
    ----------
    item : Any
        some object

    Returns
    -------
    bool
        True or False

    Examples
    --------
    >>> is_int_0_or_1(0)
    True
    >>> is_int_0_or_1([1, 2, 3])
    False
    """
    is_int = type(item) == int
    is_0_or_1 = item in LIST_ZERO_AND_ONE
    return is_int and is_0_or_1

