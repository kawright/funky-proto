"""
This module contains the implementation of the `CharStream` class, which
contains a stream of characters and defines methods for supporting
single-character scanning and look-ahead operations.
"""

from typing import TextIO

from src.Eject import ErrorEject

class CharStream:
    """
    This class contains a stream of characters and has methods which support
    single-character scanning and look-ahead operations.
    """

    def __init__(self, path:str) -> "CharStream":
        """
        Create a new instance of this class.
        
        Emits an `IO` error if the given source file cannot be opened.
        """

        self.contents:str       # The contents of the stream.
        self.cursor:int         # The position of the cursor.
        self.len:int            # The length of the stream.
        self.line:int           # The current line number.
        self.column:int         # The current column number.

        fp:TextIO               # File pointer.

        try:
            with open(path) as fp:
                self.contents = fp.read()
        except IOError:
            raise ErrorEject("ca6dba32-ad40-4c85-937a-3ffbd0001183", \
                "Could not open source code file '{}'".format(path), "IO")

        self.cursor = 0
        self.len = len(self.contents)
        self.line = 1
        self.column = 1

        return

    def advance(self) -> None:
        """
        Advance the cursor a single position forward.

        Emits an `INTERPRETER` error if the cursor is already at the end of the
        stream.
        """

        if self.end_of_stream():
            raise ErrorEject("9791ac9f-c0f6-44f1-a7ff-4cbd5db3486e", \
                "The stream has already reached the end", "INTERPRETER")
        self.cursor += 1

        return

    def end_of_stream(self) -> bool:
        """
        Test if the cursor is at the end of the stream (i.e. is the cursor
        position past the last character?)
        """

        if self.cursor >= self.len:
            return True
        return False

    def peek(self) -> str:
        """
        Return the character immediately ahead of the cursor.
        
        Return `None` if the cursor is already at the end of the stream.
        """
        if self.cursor >= (self.len - 1):
            return None
        return self.contents[self.cursor + 1]

    def pop(self) -> str:
        """
        Read the character at the cursor's position, advance the cursor, 
        then return the read character.

        Emits an `INTERPRETER` error if the cursor is already at the end of the
        stream.
        """

        if (self.end_of_stream()):
            raise ErrorEject("26754990-e2fd-4b6c-9542-a87df8d622dc", \
                "The stream has already reached the end", "INTERPRETER")

    def read(self) -> str:
        """
        Read the character at the cursor, without moving it.

        Returns `None` if the cursor is already at the end of the stream.
        """

        if self.end_of_stream():
            return None
        return self.contents[self.cursor]