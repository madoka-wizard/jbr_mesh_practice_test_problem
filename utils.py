import argparse
import itertools
import sys


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return map(tuple, zip(a, b))


def timestamp_to_milliseconds(timestamp):
    try:
        return int(timestamp)
    except ValueError:
        hours, minutes, seconds, milliseconds = map(int, timestamp.replace(',', ':').replace('.', ':').split(':'))
        return milliseconds + 1000 * (seconds + 60 * (minutes + 60 * hours))


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'Error: {message}\n')
        self.print_help()
        sys.exit(2)
