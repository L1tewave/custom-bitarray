import pytest

from bitarray.core import BitArray
from bitarray.services import is_char_0_or_1


@pytest.fixture
def x():
    return BitArray("1011")


class TestBitArray:

    def test_init(self):
        assert BitArray([True, False, 1]).bits == [True, False, True]

    def test_init_exception(self):
        with pytest.raises(TypeError):
            dictionary = dict(
                zero=False,
                one=True,
            )
            x = BitArray(dictionary.values())
        with pytest.raises(ValueError):
            x = BitArray("12012")
        with pytest.raises(ValueError):
            x = BitArray([1, 2, 0, 1, 2])

    def test_append(self, x: BitArray):
        x.append("101")
        assert x == BitArray("1011101")

    def test_equals_reflexive(self, x):
        assert x == x

    def test_equals_symmetric(self, x):
        y = BitArray([True, False, True, True])
        assert x == y

    def test_equals_transitivity(self, x):
        y = BitArray([True, False, True, True])
        z = BitArray([1, 0, 1, 1])
        assert x == y
        assert y == z
        assert x == z

    def test_equals_none(self, x):
        assert x is not None

    def test_equals_not_equal(self, x):
        y = BitArray([True, False, True, True, True])
        assert x != y

    def test_equals_float(self, x):
        assert (x == 1.0) is False

    @pytest.mark.parametrize("actual, expected",
                             [(BitArray("111"), BitArray("000")), (BitArray("101010"), BitArray("010101"))])
    def test_not(self, actual, expected):
        assert ~actual == expected

    def test_and(self):
        x = BitArray("10101")
        y = BitArray("01100")
        z = BitArray("00100")

        assert x & y == z

    def test_and_exception(self, x):
        with pytest.raises(TypeError):
            y = x & "something else"
        with pytest.raises(ValueError):
            y = x & BitArray()

    def test_or(self):
        x = BitArray("10101")
        y = BitArray("01100")
        z = BitArray("11101")

        assert x | y == z

    def test_or_exception(self, x):
        with pytest.raises(TypeError):
            y = x | "something else"
        with pytest.raises(ValueError):
            y = x | BitArray()

    def test_implication(self):
        x = BitArray("10101")
        y = BitArray("01100")
        z = BitArray("01110")

        assert x.implies(y) == z

    def test_implication_exception(self, x):
        with pytest.raises(TypeError):
            y = x.implies("something else")
        with pytest.raises(ValueError):
            y = x.implies(BitArray())

    def test_equivalence(self):
        x = BitArray("10101")
        y = BitArray("01100")
        z = BitArray("00110")

        assert x.equals(y) == z

    def test_equivalence_exception(self, x):
        with pytest.raises(TypeError):
            y = x.equals("something else")
        with pytest.raises(ValueError):
            y = x.equals(BitArray())

    def test_representation(self, x):
        x = BitArray([True] * 10)
        assert repr(x) == f"BitArray <{str(1) * 10}> object"

    # Equivalence classes.
    # Separation on the basis of "there is an inversion sign - there is no inversion sign".
    # The types of operations are also tested.
    def test_execute_neutral_neutral(self):
        x = BitArray.execute("100101 & 111001")
        assert x == BitArray("100001")

    def test_execute_neutral_inverse(self):
        x = BitArray.execute("100101 & ~111001")
        assert x == BitArray("000100")

    def test_execute_inverse_neutral(self):
        x = BitArray.execute("~100101 & 111001")
        assert x == BitArray("011000")

    def test_execute_inverse_inverse(self):
        x = BitArray.execute("~100101 & ~111001")
        assert x == BitArray("000010")

    def test_execute_bitwise_or(self):
        x = BitArray.execute("100101 | ~111001")
        assert x == BitArray("100111")

    def test_execute_bitwise_implication(self):
        x = BitArray.execute("~100101 -> 111001")
        assert x == BitArray("111101")

    def test_execute_bitwise_equivalence(self):
        x = BitArray.execute("~100101 = ~111001")
        assert x == BitArray("100011")

    def test_execute_unsupported_operation(self):
        assert BitArray.execute("10 ) 10") is None

    def test_execute_different_length_operands(self):
        assert BitArray.execute("10 = 101") is None

    def test_execute_whitespaces(self):
        x = BitArray.execute(" 1011   |   1101   ")
        assert x == BitArray("1111")

    def test_execute_bad_format_one_argument(self):
        assert BitArray.execute("101011") is None

    def test_execute_bad_format_one_argument_and_operation(self):
        assert BitArray.execute("101011 >") is None

    def test_execute_bad_format_three_arguments(self):
        assert BitArray.execute("1 & 1 & 0") is None

    def test_execute_bad_format_empty_string(self):
        assert BitArray.execute("") is None

    def test_execute_none(self):
        assert BitArray.execute(None) is None

    def test_execute_gibberish(self):
        assert BitArray.execute("dsaw0re1_~!0`-012`32213_*@#&&*~as' wsad") is None


def test_single_character_exception():
    with pytest.raises(ValueError):
        is_char_0_or_1("not a single character")
