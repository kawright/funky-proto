"""
This module contains the implementation of the `Token` class, which is an enum
class that stores all of the token types that constitute the `Funky` language.
"""

import enum

class Token(enum.Enum):
    """
    This enum class stores all of the token types that constitute the `Funky` 
    language.
    """

    COMMA = enum.auto()
    EQUALS = enum.auto()
    LEFT_ANGLE = enum.auto()
    LEFT_BRACKET = enum.auto()
    LEFT_PAREN = enum.auto()
    RIGHT_ANGLE = enum.auto()
    RIGHT_BRACKET = enum.auto()
    RIGHT_PAREN = enum.auto()
    SEMICOLON = enum.auto()
    STRING = enum.auto()
    SYMBOL = enum.auto()
