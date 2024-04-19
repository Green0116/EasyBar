class EasyBarException(Exception):
    """Base runtime exception for EasyBar."""


class EasyBarFileNotFoundError(EasyBarException):
    """Exception raised when the configuration file is not found."""


class EasyBarDecodeError(EasyBarException):
    """Exception raised when the configuration file cannot be decoded."""


class EasyBarTypeError(EasyBarException):
    """Exception raised when an object is not of the expected type."""


class EasyBarValueError(EasyBarException):
    """Exception raised when an object has an invalid value."""


class EasyBarKeyError(EasyBarException):
    """Exception raised when a key is not found in a dictionary."""


class EasyBarStopIteration(StopIteration, EasyBarException):
    """Exception raised when the iteration is stopped."""


class EasyBarNotImplementedError(NotImplementedError, EasyBarException):
    """Exception raised when a method is not implemented."""
