#!/usr/bin/env sh

set -o errexit
set -o nounset
cmd="$*"
exec ./simple_audio_processor.py $cmd
