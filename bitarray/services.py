from bitarray.settings import STR_ZERO_AND_ONE, CHAR_LENGTH, LIST_ZERO_AND_ONE


def is_char_0_or_1(char: str) -> bool:
    if len(char) != CHAR_LENGTH:
        raise ValueError("Function must be called for single characters")
    return char in STR_ZERO_AND_ONE


def is_bool(item) -> bool:
    return isinstance(item, bool)


def is_int_0_or_1(item) -> bool:
    is_int = type(item) == int
    is_0_or_1 = item in LIST_ZERO_AND_ONE
    return is_int and is_0_or_1

