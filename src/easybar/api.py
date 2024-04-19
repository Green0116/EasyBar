from .utils import Bar, colour_txt, Numeric
from .exceptions import EasyBarException

from typing import Optional, Callable
import time as _time


class EasyBar(Bar):

    def __init__(self, total: Numeric, *args, **kwargs):
        super().__init__(total, *args, **kwargs)

        # Progress to be updated
        self._inc = 1

    def update(self):
        with self._lock:
            self._progress += self._inc
            self.print_bar()

    def print_bar(self):
        progress = self._progress / self._total

        if self._mode == 'fraction':
            progress_str = f'{self._progress} / {self._total}'
        else:
            progress_str = f'{(progress * 100):.2f}%'

        prefix_len = len(self.prefix)
        progress_len = len(progress_str)
        boundary_len = len(self._boundary)
        bar_len = self._window_size - prefix_len - \
            progress_len - boundary_len - self._margin
        display_len = int(bar_len * progress)
        fill_len = bar_len - display_len

        prefix = self._prefix
        display = self._display * display_len
        fill = self._fill * fill_len
        start, end = self._boundary

        bar = '\r' + prefix + start + display + fill + \
            end + progress_str

        print(colour_txt(bar), end='', flush=True)

    def inc(self, inc):
        self._inc = inc


def retry(func: Callable, max: Optional[int] = None,
          *args, **kwargs) -> Callable:
    def inner(*args, **kwargs):
        bar = EasyBar(max, *args, **kwargs)

        for _ in bar:
            try:
                res = func(*args, **kwargs)
                break
            except Exception as e:
                msg = f'Failed to execute {func.__name__}: {e}'

            _time.sleep(0)
        else:
            msg = f'Failed to execute {func.__name__} after {max} retries'

            raise EasyBarException(msg)

        return res

    return inner


def loop(func: Callable, times: Optional[int] = None,
         *args, **kwargs) -> Callable:
    _args = args
    _kwargs = kwargs

    def inner(*args, **kwargs):
        if times is not None:
            remaining = times
        else:
            remaining = float("inf")

        for _ in Bar(remaining, _args, _kwargs):
            try:
                yield func(*args, **kwargs)
            except Exception as e:
                msg = f'Failed to execute {func.__name__}: {e}'

                raise EasyBarException(msg)

    return inner
