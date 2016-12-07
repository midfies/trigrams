"""Test module for trigrams.py"""

import pytest


def test_input_file():
    from trigram import input_file
    assert input_file(src/sample.txt) != ""
