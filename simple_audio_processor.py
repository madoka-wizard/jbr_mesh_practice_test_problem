#!/usr/bin/env python
import os
import sys

from app import concat_audio_files, cut_audio_file, break_up_audio_file_by_timestamps, reverse_audio_file
from utils import timestamp_to_milliseconds, MyParser


def execute(command, args):
    if command == 'concat':
        concat_audio_files(audio_files=args.audio_files, out_file=args.out)

    elif command == 'cut':
        with open(args.intervals) as intervals_file:
            intervals = (map(timestamp_to_milliseconds, line.split(',')) for line in intervals_file.readlines())
            cut_audio_file(audio_file=args.audio_file, intervals=intervals)

    elif command == 'ts':
        with open(args.stamps) as timestamps_file:
            timestamps = map(timestamp_to_milliseconds, timestamps_file.readlines())
            break_up_audio_file_by_timestamps(audio_file=args.audio_file, timestamps=timestamps)

    elif command == 'reverse':
        if args.out:
            reverse_audio_file(args.audio_file, args.out)
        else:
            audio_file_name, audio_file_extension = os.path.splitext(args.audio_file)
            reverse_audio_file(args.audio_file, f'{audio_file_name}_reversed{audio_file_extension}')


def main():
    main_parser = MyParser(description='Primitive audio processing tool.', add_help=False)
    main_parser.add_argument('-h', '--help', action='help', help='Show this help message and exit.')
    commands_parser = main_parser.add_subparsers(dest='cmd', metavar="COMMAND", help='Description')

    concat_command = commands_parser.add_parser('concat', help='Concatenate multiple audio files.')
    concat_command.add_argument('audio_files', metavar='INPUT_FILE', type=str, nargs='+')
    concat_command.add_argument('out', metavar='OUTPUT_FILE', type=str)

    cut_command = commands_parser.add_parser('cut', help='Split audio file into interval pieces.')
    cut_command.add_argument('audio_file', metavar='INPUT_FILE', type=str)
    cut_command.add_argument('intervals', metavar='INTERVALS_FILE', type=str)

    timestamps_command = commands_parser.add_parser('ts', help='Break up audio file by timestamps.')
    timestamps_command.add_argument('audio_file', metavar='INPUT_FILE', type=str)
    timestamps_command.add_argument('timestamps', metavar='TS_FILE', type=str)

    reverse_command = commands_parser.add_parser('reverse', help='Reverse audio file.')
    reverse_command.add_argument('audio_file', metavar='INPUT_FILE', type=str)
    reverse_command.add_argument('--out', metavar='OUTPUT_FILE', type=str)

    if len(sys.argv) < 2:
        main_parser.print_help(sys.stderr)
        sys.exit(1)

    args = main_parser.parse_args()
    if not args:
        print(args, file=sys.stderr)
    else:
        try:
            execute(args.cmd, args)
        except Exception as e:
            print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
