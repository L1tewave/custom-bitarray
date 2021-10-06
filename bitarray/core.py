# a b c d e f g h i j k l m n o p q r s t u v w x y z
"""
Class implementation
"""
from __future__ import annotations

from typing import List
from typing import Union

from bitarray.services import is_char_0_or_1, is_bool, is_int_0_or_1
from bitarray.settings import NoneType


# For methods documentation
METHODS_TO_BE_DOCUMENTED = [
    "__or__", "__and__",
    "__invert__", "__eq__",
    "__ne__", "__len__",
    "_parse_str", "_parse_list",
]

__pdoc__ = {"BitArray." + method: True for method in METHODS_TO_BE_DOCUMENTED}


class BitArray:
    """
    Bit array class

    Stores bit values as a list with boolean values
    """

    def __init__(self, initializer: Union[List, str, None] = None):
        if not isinstance(initializer, (list, str, NoneType)):
            raise ValueError(f"Unsupported initializer type {type(initializer)}")

        if isinstance(initializer, str):
            self.__bits = BitArray._parse_str(initializer)
        if isinstance(initializer, List):
            self.__bits = BitArray._parse_list(initializer)
        if isinstance(initializer, NoneType):
            self.__bits = []

    @property
    def bits(self) -> List[bool]:
        """
        Returns the bit values
        """
        return self.__bits

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
            implication result

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
        if not isinstance(other, BitArray):
            raise TypeError("BitArray does not support <implication> "
                            "with all types other than BitArray")
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
            bitwise or result

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
        if not isinstance(other, BitArray):
            raise TypeError("BitArray does not support <bitwise or> "
                            "with all types other than BitArray")
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
            bitwise and result

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
        if not isinstance(other, BitArray):
            raise TypeError("BitArray does not support <bitwise and> "
                            "with all types other than BitArray")
        return BitArray([x and y for x, y in zip(self.bits, other.bits)])

    def __invert__(self) -> BitArray:
        """
        Invert Bitarray object

        Returns
        -------
        BitArray
            bitwise not result

        Examples
        --------
        >>> x = BitArray("1011")
        >>> ~x
        BitArray <0100> object
        """
        return BitArray([not x for x in self.bits])

    def __eq__(self, other: BitArray) -> bool:
        """
        Checks the equality of two BitArrays

        Parameters
        ----------
        other : BitArray
            another array of bytes

        Returns
        -------
        bool
            compare result

        Note
        ----
        When an invalid type is passed, it returns False

        Examples
        --------
        >>> x = BitArray("1011")
        >>> y = BitArray("1011")
        >>> x == y
        True
        >>> x == "1011"
        False
        """
        if not isinstance(other, BitArray):
            return False
        if len(self) != len(other):
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
        if all(map(is_bool, lst)):
            return lst
        if all(map(is_int_0_or_1, lst)):
            return list(map(bool, lst))
        raise ValueError("The List must contain only digits [0, 1] or only boolean values [False, True]")
