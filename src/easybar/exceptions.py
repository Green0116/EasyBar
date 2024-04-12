class EasyBarException(Exception):
    """Base exception for EasyBar."""


class EasyBarKeyboardInterrupt(KeyboardInterrupt, EasyBarException):
    """Exception raised when the user interrupts the program."""


class EasyBarTypeError(EasyBarException):
    """Exception raised when an object is not of the expected type."""


class EasyBarValueError(EasyBarException):
    """Exception raised when an object has an invalid value."""


class EasyBarKeyError(EasyBarException):
    """Exception raised when a key is not found in a dictionary."""
