"""Test module for trigrams.py."""

# import pytest


def test_input_file():
    from trigrams import input_file
    assert input_file('sample.txt') != ""
