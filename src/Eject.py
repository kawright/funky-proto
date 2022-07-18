"""
This module contains the implementation of the `Eject` class, which is a 
specific type of Exception that is used to interrupt a program's flow--such as 
when returning or throwing an error--or to signal an error and terminate 
execution. It also contains the implementations of all subclasses of `Eject`.
"""

class Eject(Exception):
    """This is the base-class for all other ejects."""

    def __init__(self, msg:str) -> "Eject":
        """Create a new instance of this class."""

        self.name:str           # The name of this eject
        self.msg:str            # A descriptive message for this eject.

        super().__init__(msg)
        self.name = "Eject"
        return

class ErrorEject(Eject):
    """This eject is used to signal the occurrence of a runtime error."""

    def __init__(self, traceid:str, \
            msg:str="A general runtime error occurred.", categ:str="GENERAL"):
        """Create a new instance of this class."""

        self.name:str           # The name of this eject
        self.msg:str            # A descriptive message for this eject.
        self.categ:str          # The error category, such as TYPE, SYNTAX, etc.
        self.traceid:str        # Used to find relevant src code from errors.

        super().__init__(msg)
        self.name = "ErrorEject"
        self.categ = categ
        self.traceid = traceid
        return
