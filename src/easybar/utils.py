from .exceptions import (
    EasyBarKeyError,
    EasyBarStopIteration,
    EasyBarFileNotFoundError,
    EasyBarDecodeError,
    EasyBarValueError,
    EasyBarNotImplementedError,
)

import shutil as _shutil
from multiprocessing import Lock as _lock
import json
from typing import Optional, Union


# Global progress lock
PROGRESS_LOCK = _lock()
# Default colour sequence configuration file
COLOUR_CONFIG_FILE = '../config/colour_sequence.json'
# Numeric type for int and float
Numeric = Union[int, float]

# ANSI escape sequences for console
# text and background colours
try:
    with open(COLOUR_CONFIG_FILE, 'r') as json_file:
        COLOUR_SEQUENCE = json.load(json_file)
except FileNotFoundError as e:
    msg = f'Failed to load colour sequence file: {COLOUR_CONFIG_FILE}'

    raise EasyBarFileNotFoundError(msg) from e
except json.JSONDecodeError:
    msg = f'Cannot decode colour sequence file: {COLOUR_CONFIG_FILE}'

    raise EasyBarDecodeError(msg)


class Bar:

    def __init__(self, total: Numeric, mode: str = 'default',
                 prefix: Optional[str] = None, display: str = '█',
                 fill: str = ' ', margin: int = 2, boundary: str = '[]',
                 colour: str = 'default', bg_colour: str = 'default'):
        self._total = total

        # Currently support percentage and fraction modes
        if mode in ('default', 'fraction', 'f'):
            self._mode = 'fraction'
        elif mode in ('percentage', 'p'):
            self._mode = 'percentage'
        else:
            msg = f'Invalid mode: {mode}'

            raise EasyBarValueError(msg)

        if prefix is None:
            self._prefix = 'EasyBar: '
        else:
            self._prefix = prefix

        self._display = display
        self._fill = fill
        self._margin = margin

        # Boundary must be a pair of start and end characters
        boundary_len = len(boundary)

        if boundary_len != 2:
            msg = (
                'Boundary must be two characters, '
                f'got {boundary_len}: {boundary}'
            )

            raise EasyBarValueError(msg)

        self._boundary = boundary
        self._colour = colour
        self._bg_colour = bg_colour

        self._progress = 0
        self._window_size = self.get_window_size()
        self._is_complete = False
        self._lock = PROGRESS_LOCK

    def __iter__(self):
        return self

    def __next__(self):
        if self._progress >= self._total:
            self._is_complete = True
            print()

            raise EasyBarStopIteration

        self.update()

        return self._progress

    def update(self, prog: Numeric):
        """Update the progress bar."""
        raise EasyBarNotImplementedError

    def is_complete(self):
        return self._is_complete

    @staticmethod
    def get_window_size():
        return _shutil.get_terminal_size().columns

    @staticmethod
    def colour_txt(text: str, foreground: str = 'default',
                   background: str = 'default') -> str:
        foreground = foreground.lower()
        background = background.lower()

        if foreground not in COLOUR_SEQUENCE['foreground']:
            msg = f'Invalid text colour: {foreground}'

            raise EasyBarKeyError(msg)

        if background not in COLOUR_SEQUENCE['background']:
            msg = f'Invalid background colour: {background}'

            raise EasyBarKeyError(msg)

        txt_colour = COLOUR_SEQUENCE['foreground'][foreground]
        bg_colour = COLOUR_SEQUENCE['background'][background]
        reset = COLOUR_SEQUENCE['foreground']['reset']
        coloured_text = txt_colour + bg_colour + text + reset

        return coloured_text
