import argparse
import itertools
import sys
from typing import Iterable


def pairwise(iterable: Iterable) -> Iterable:
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def timestamp_to_milliseconds(timestamp: str) -> int:
    try:
        return int(timestamp)
    except ValueError:
        hours, minutes, seconds, milliseconds = [int(x) for x in timestamp.replace(',', ':').split(':')]
        return milliseconds + 1000 * (seconds + 60 * (minutes + 60 * hours))


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'Error: {message}\n')
        self.print_help()
        sys.exit(2)
