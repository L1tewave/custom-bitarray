# a b c d e f g h i j k l m n o p q r s t u v w x y z
"""
Class implementation
"""
from __future__ import annotations

from typing import List
from typing import Union

from bitarray.services import is_bool
from bitarray.services import is_char_0_or_1
from bitarray.services import is_int_0_or_1


class BitArray:
    """
    Bit array class

    Stores bit values as a list with boolean values
    """
    ALLOWED_TYPES = (list, str)

    def __init__(self, initializer: Union[list, str, None] = None):
        self.__bits = []

        if not initializer:
            return

        self.__bits += self._try_parse(initializer)

    @property
    def bits(self) -> List[bool]:
        """
        Returns the bit values
        """
        return self.__bits

    def append(self, new_bits: Union[list, str]) -> None:
        """
        Adds values to the end of the array

        Parameters
        ----------
        new_bits : List[int] / List[bool] / str
            values to be added

        Returns
        -------
        None

        Raises
        ------
        TypeError
            when an invalid data type is transmitted

        Examples
        --------
        >>> x = BitArray("1011")
        >>> x.append("1100")
        >>> x
        BitArray <11011100> object
        """
        self.__bits += self._try_parse(new_bits)

    def implies(self, other: BitArray) -> BitArray:
        """
        Implements a bitwise implication

        Parameters
        ----------
        other : BitArray
            another array of bytes

        Returns
        -------
        BitArray
            new BitArray object, result of "implication (x -> y)"

        Raises
        ------
        TypeError
            when an invalid data type is transmitted

        Examples
        --------
        >>> x = BitArray("1011")
        >>> y = BitArray("1100")
        >>> x.implies(y)
        BitArray <1100> object
        """
        self._check_support(other, "bitwise implication")
        return ~self | other

    def __or__(self, other: BitArray) -> BitArray:
        """
        Implements a bitwise or

        Parameters
        ----------
        other : BitArray
            another array of bytes

        Returns
        -------
        BitArray
            new BitArray object, result of "bitwise or"

        Raises
        ------
        TypeError
            when an invalid data type is transmitted

        Examples
        --------
        >>> x = BitArray("1011")
        >>> y = BitArray("1100")
        >>> x | y
        BitArray <1111> object
        """
        self._check_support(other, "bitwise or")
        return BitArray([x or y for x, y in zip(self.bits, other.bits)])

    def __and__(self, other: BitArray) -> BitArray:
        """
        Implements a bitwise and

        Parameters
        ----------
        other : BitArray
            another array of bytes

        Returns
        -------
        BitArray
            new BitArray object, result of "bitwise and"

        Raises
        ------
        TypeError
            when an invalid data type is transmitted

        Examples
        --------
        >>> x = BitArray("1011")
        >>> y = BitArray("1100")
        >>> x & y
        BitArray <1000> object
        """
        self._check_support(other, "bitwise and")
        return BitArray([x and y for x, y in zip(self.bits, other.bits)])

    def __invert__(self) -> BitArray:
        """
        Invert Bitarray object

        Returns
        -------
        BitArray
            new BitArray object, result of "bitwise not"

        Examples
        --------
        >>> x = BitArray("1011")
        >>> ~x
        BitArray <0100> object
        """
        return BitArray([not x for x in self.bits])

    def __eq__(self, other: BitArray) -> bool:
        """
        Checks for equality with another object

        Parameters
        ----------
        other : Any
            some object

        Returns
        -------
        bool
            comparison result

        Note
        ----
        When an invalid type (not BitArray) is passed, it returns False

        Examples
        --------
        >>> x = BitArray("1011")
        >>> y = BitArray("1011")
        >>> x == y
        True
        >>> x == "1011"
        False
        """
        if not isinstance(other, BitArray) or len(self) != len(other):
            return False
        return self.bits == other.bits

    def __ne__(self, other: BitArray) -> bool:
        """
        Same as the equality check, only it returns the opposite result
        """
        return not self == other

    def __repr__(self) -> str:
        representation = "".join(map(str, map(int, self.bits)))
        return f"BitArray <{representation}> object"

    def __len__(self):
        """
        Length of the list of bytes

        Examples
        --------
        >>> x = BitArray("1011")
        >>> len(x)
        4
        """
        return len(self.bits)

    def _check_support(self, other: BitArray, operation: str) -> None:
        """
        Auxiliary function to check that bitwise and, bitwise or
        and bitwise implication operations can be performed

        Parameters
        ----------
        other : Any
            some object

        Raises
        ------
        ValueError
            when the lengths of the BitArray objects do not match

        TypeError
            when an incorrect type is transmitted
        """
        if not isinstance(other, BitArray):
            raise TypeError(f"BitArray does not support <{operation}> "
                            "with all types other than BitArray")
        if len(self) != len(other):
            raise ValueError("Operands of different lengths!")

    def _try_parse(self, new_bits) -> List[bool]:
        """
        If possible converts the argument into an array of bits

        Parameters
        ----------
        new_bits : Any
            some object

        Raises
        ------
        ValueError
            when conversion is not possible

        TypeError
            when an incorrect type is transmitted
        """
        self._check_type(new_bits)
        parse = self._parse_str if type(new_bits) == str else self._parse_list
        return parse(new_bits)

    @staticmethod
    def _parse_str(string: str) -> List[bool]:
        """
        Checks if the transmitted string can be converted to an array of bytes

        Parameters
        ----------
        string : str
            string to check

        Returns
        -------
        List[bool]
            byte array

        Raises
        ------
        ValueError
            when conversion is not possible

        Examples
        --------
        >>> ByteArray._parse_str("1011")
        [True, False, True, True]
        """
        if not all(map(is_char_0_or_1, string)):
            raise ValueError("Initializer must consist of 0 and 1 only")
        return list(map(bool, map(int, string)))

    @classmethod
    def _parse_list(cls, lst: list) -> List[bool]:
        """
        Checks if the transmitted list can be converted to an array of bytes

        The list must contain digits: [0, 1] or boolean values: [False, True]

        Parameters
        ----------
        lst : List[bool], List[int]
            list to check

        Returns
        -------
        List[bool]
            byte array

        Raises
        ------
        ValueError
            when conversion is not possible

        Examples
        --------
        >>> ByteArray._parse_list([1, 0, 1, 1])
        [True, False, True, True]
        """
        is_bit = lambda bit: is_bool(bit) or is_int_0_or_1(bit)

        if not all(map(is_bit, lst)):
            raise ValueError("The list must contain digits: [0, 1] or boolean values: [False, True]")

        return list(map(bool, lst))

    @classmethod
    def _check_type(cls, new_bits) -> None:
        """
        Checks if the passed argument belongs to a valid type

        Parameters
        ----------
        new_bits : Any
            some object

        Raises
        ------
        TypeError
            when an incorrect type is transmitted
        """
        if isinstance(new_bits, cls.ALLOWED_TYPES):
            return
        raise TypeError(f"Expected one of these types {cls.ALLOWED_TYPES}, got {type(new_bits)} instead")
