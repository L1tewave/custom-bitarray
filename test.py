import pytest

from bitarray.core import BitArray


@pytest.fixture
def x():
    return BitArray("1011")


class TestBitArray:

    def test_init_exception(self):
        with pytest.raises(ValueError):
            x = BitArray("12012")

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

    def test_or(self):
        x = BitArray("10101")
        y = BitArray("01100")
        z = BitArray("11101")

        assert x | y == z

    def test_or_exception(self, x):
        with pytest.raises(TypeError):
            y = x | "something else"

    def test_implication(self):
        x = BitArray("10101")
        y = BitArray("01100")
        z = BitArray("01110")

        assert x.implies(y) == z

    def test_implication_exception(self, x):
        with pytest.raises(TypeError):
            y = x.implies("something else")
