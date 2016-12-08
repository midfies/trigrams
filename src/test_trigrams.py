"""Test module for trigrams.py."""

# import pytest


def test_input_file():
    from trigrams import input_file
    assert input_file('sample.txt') is not ''


def test_get_sentences():
    sample = """This * is - sentence one. This is sentence two. This is sentence \
three."""
    from trigrams import split_data
    assert split_data(sample)[0] == """This * is - sentence one"""


def test_remove_punc():
    sample_sent = 'This * is - sentence one'
    from trigrams import remove_punc
    assert '*' not in remove_punc(sample_sent)


def test_get_words():
    sample_split = "This  is  sentence one"
    from trigrams import split_words
    assert split_words(sample_split) == ['This', 'is', 'sentence', 'one']


def test_add_to_empty_dic():
    empty_dic = {}
    from trigrams import add_to_dic
    assert add_to_dic(empty_dic, 'key', 1) == {'key': [1]}


def test_found_key():
    dic = {'key': [1]}
    from trigrams import add_to_dic
    assert add_to_dic(dic, 'key', 2) == {'key': [1, 2]}


def test_new_key():
    dic = {'key': [1]}
    from trigrams import add_to_dic
    assert add_to_dic(dic, 'key2', 3) == {'key': [1], 'key2': [3]}


def test_select_rand_key():
    dic = {'key1': 1, 'key2': 2, 'key3': 3}
    from trigrams import select_rand_key
    assert select_rand_key(dic) in dic
