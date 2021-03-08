import itertools
import os

from pydub import AudioSegment

from utils import pairwise


def concat_audio_files(audio_files, out_file):
    _, out_file_ext = os.path.splitext(out_file)
    audio_segments = (AudioSegment.from_file(file) for file in audio_files)
    return sum(audio_segments).export(out_file, format=out_file_ext[1:])


def cut_audio_segment(audio_segment, intervals):
    return (audio_segment[interval[0]:interval[1]] for interval in intervals)


def cut_audio_file(audio_file, intervals):
    audio_file_name, audio_file_extension = os.path.splitext(audio_file)
    audio_segment = AudioSegment.from_file(audio_file)
    return (current.export(f'{audio_file_name}_{idx}{audio_file_extension}', format=audio_file_extension[1:])
            for idx, current in enumerate(cut_audio_segment(audio_segment, intervals)))


def break_up_audio_file_by_timestamps(audio_file, timestamps):
    audio_file_name, audio_file_ext = os.path.splitext(audio_file)
    audio_segment = AudioSegment.from_file(audio_file)
    intervals = pairwise(itertools.chain((0,), timestamps, len(audio_segment)))
    return (current.export(f'{audio_file_name}_{idx}{audio_file_ext}', format=audio_file_ext[1:])
            for idx, current in enumerate(cut_audio_segment(audio_segment, intervals)))


def reverse_audio_file(audio_file, out_file):
    _, out_file_ext = os.path.splitext(out_file)

    return AudioSegment.from_file(audio_file).reverse().export(out_file, format=out_file_ext[1:])
