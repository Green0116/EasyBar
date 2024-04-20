import argparse
import time as _time

from .api import EasyBar
from .version import __version__


def main():
    parser = argparse.ArgumentParser(description='EasyBar')
    parser.add_argument('-d', '-demo', action='store_true')
    parser.add_argument('--v', '--version', action='store_true')
    args = parser.parse_args()

    if args.d:
        demo = EasyBar()

        for _ in demo:
            _time.sleep(0.01)
    elif args.v:
        print(__version__)
    else:
        pass


if __name__ == '__main__':
    main()
