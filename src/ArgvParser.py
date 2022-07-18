"""
This module contains th implementation of the `ArgvParser` class, which is used
to parse the argument vector in order to yield the passed in command-line
arguments.
"""

import argparse

from src.Eject import ErrorEject

class _EjectParser(argparse.ArgumentParser):
    """This class overrides the error behavior such that an eject is emitted."""

    def error(self, message):
        raise ErrorEject("4bc01e70-926b-4be5-b222-84d2fda56667", \
            "Invalid arguments/options given", "COMMAND_LINE")

class ArgvParser:
    """
    This class is used for parsing the argument vector in order to yield the
    passed in command-line arguments, which are stored as instance attributes.

    Raises `ErrorEject` if invalid command-line arguments are given.
    """

    def __init__(self) -> "ArgvParser":
        """Create a new instance of this class."""
        
        self.src_path:str               # The path to the source code file

        args:argparse.Namespace         # Parsed args
        parser:argparse.ArgumentParser  # `argparse` parser

        # Use `argparse` to parse the argv:
        parser = argparse.ArgumentParser()
        parser.add_argument("path", type=str)
        args = parser.parse_args()

        # Initialize attributes:
        self.src_path = args
        
        return