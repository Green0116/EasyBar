class EasyBarException(Exception):
    """Base exception for EasyBar."""


class EasyBarKeyboardInterrupt(KeyboardInterrupt, EasyBarException):
    """Exception raised when the user interrupts the program."""


class EasyBarConfigurationError(EasyBarException):
    """Exception raised when the configuration is invalid."""


class EasyBarTypeError(EasyBarException):
    """Exception raised when an object is not of the expected type."""


class EasyBarValueError(EasyBarException):
    """Exception raised when an object has an invalid value."""


class EasyBarKeyError(EasyBarException):
    """Exception raised when a key is not found in a dictionary."""


class EasyBarIndexError(EasyBarException):
    """Exception raised when an index is out of range."""


class EasyBarStopIteration(EasyBarException):
    """Exception raised when the iteration is stopped."""


class EasyBarNotFoundError(EasyBarException):
    """Exception raised when an object is not found."""
