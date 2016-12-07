"""Test module for trigrams.py."""

# import pytest
sample = """This * is - sentence one. This is sentence two. This is sentence \
three."""
sample_sent = 'This * is - sentence one'


def test_input_file():
    from trigrams import input_file
    assert input_file('sample.txt') is not ''


def test_get_sentences():
    from trigrams import split_data
    assert split_data(sample)[0] == """This * is - sentence one"""


def test_remove_punc():
    from trigrams import remove_punc
    assert '*' not in remove_punc(sample_sent)
