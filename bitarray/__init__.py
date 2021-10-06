"""
Package with a custom BitArray class that contains
implementations of bitwise and, bitwise or, bitwise negation and bitwise implication

author: Igor Kostychakov

version: 1.1.1
"""
__author__ = "Igor Kostychakov"

__version__ = "1.1.1"

# For methods documentation
METHODS_TO_BE_DOCUMENTED = [
    "__or__", "__and__",
    "__eq__", "__len__",
    "__ne__", "__invert__" 
    "_parse_str", "_parse_list",
    "_check_support", "_check_type",
    "_try_parse",
]

__pdoc__ = {"bitarray.core.BitArray." + method: True for method in METHODS_TO_BE_DOCUMENTED}
