# a b c d e f g h i j k l m n o p q r s t u v w x y z
from __future__ import annotations

from typing import List
from typing import Union

from bitarray.services import is_char_0_or_1, is_bool, is_int_0_or_1
from bitarray.settings import NoneType


class BitArray:

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
    def bits(self):
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
        """
        if not isinstance(other, BitArray):
            raise TypeError("BitArray does not support <implication> "
                            "with all types other than BitArray")
        return ~self | other

    def __or__(self, other: BitArray) -> BitArray:
        if not isinstance(other, BitArray):
            raise TypeError("BitArray does not support <bitwise or> "
                            "with all types other than BitArray")
        return BitArray([x or y for x, y in zip(self.bits, other.bits)])

    def __and__(self, other: BitArray) -> BitArray:
        if not isinstance(other, BitArray):
            raise TypeError("BitArray does not support <bitwise and> "
                            "with all types other than BitArray")
        return BitArray([x and y for x, y in zip(self.bits, other.bits)])

    def __invert__(self) -> BitArray:
        return BitArray([not x for x in self.bits])

    def __eq__(self, other: BitArray) -> bool:
        if not isinstance(other, BitArray):
            return False
        if len(self) != len(other):
            return False
        return self.bits == other.bits

    def __ne__(self, other: BitArray) -> bool:
        return not self == other

    def __repr__(self) -> str:
        representation = "".join(map(str, map(int, self.bits)))
        return f"BitArray <{representation}> object"

    def __len__(self):
        return len(self.bits)

    @staticmethod
    def _parse_str(string: str) -> List[bool]:
        if not all(map(is_char_0_or_1, string)):
            raise ValueError("Initializer must consist of 0 and 1 only")
        return list(map(bool, map(int, string)))

    @classmethod
    def _parse_list(cls, lst: list) -> List[bool]:
        if all(map(is_bool, lst)):
            return lst
        if all(map(is_int_0_or_1, lst)):
            return list(map(bool, lst))
        raise ValueError("The List must contain only digits [0, 1] or only boolean values [False, True]")
