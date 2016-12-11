"""Test module for trigrams.py."""


def test_main_is_string():
    """Test main function returns a string."""
    from trigrams import main
    assert isinstance(main('src/sample.txt', 500), str)


def test_main_returns_correct_number():
    """Test main function returns a string."""
    from trigrams import main
    assert len((main('src/sample.txt', 100)).split()) == 100


def test_input_file():
    """Test that input_file returns a non empty string."""
    from trigrams import input_file
    assert input_file('src/sample.txt') is not ''


def test_split_data():
    """Test that split_data splits the file by sentences."""
    from trigrams import split_data
    sample = "This is sentence one. This is sentence two. This is sentence three."

    assert split_data(sample) == ['This is sentence one', ' This is sentence two', ' This is sentence three', '']


def test_build_dic_returns_dict():
    """Test the build dictionary -  Filters all words into dictionary."""
    from trigrams import build_dic
    sample = ['This * is - sentence one', 'Another test']
    assert build_dic(sample) == {'this is': ['sentence'], 'is sentence': ['one'], 'sentence one': ['.'], 'another test': ['.']}


def test_build_book_is_string():
    """Test that build_book returns a string."""
    from trigrams import build_book
    sample = {'this is': ['sentence'], 'is sentence': ['one'], 'sentence one': ['.']}
    assert isinstance(build_book(sample, 10), str)


def test_build_book_contains_words():
    """Test that build_book adds words from the dictionary."""
    from trigrams import build_book
    sample = {'this is': ['sentence'], 'is sentence': ['one'], 'sentence one': ['.']}
    assert 'this' and 'sentence' and 'is' and 'one' in build_book(sample, 10)


def test_remove_punc():
    """Test that remove_punc removes punctuation from sentences."""
    from trigrams import remove_punc
    sample_sent = 'This * is - sentence one'
    assert '*' and '-' not in remove_punc(sample_sent)


def test_get_words():
    """Test that split_words splits sentences into a list of words."""
    from trigrams import split_words
    sample_split = "This  is  sentence one"
    assert split_words(sample_split) == ['This', 'is', 'sentence', 'one']


def test_add_to_empty_dic():
    """Test that add_to_dic adds a key value pair to a dictionary."""
    from trigrams import add_to_dic
    empty_dic = {}
    assert add_to_dic(empty_dic, 'key', 1) == {'key': [1]}


def test_found_key():
    """Test that add_to_dic adds to the list value of a key if key exists."""
    from trigrams import add_to_dic
    dic = {'key': [1]}
    assert add_to_dic(dic, 'key', 2) == {'key': [1, 2]}


def test_new_key():
    """Test that add_to_dic adds new key to dictiony if key does not exist."""
    from trigrams import add_to_dic
    dic = {'key': [1]}
    assert add_to_dic(dic, 'key2', 3) == {'key': [1], 'key2': [3]}


def test_select_rand_key():
    """Test that select_rand_key gets a random key from dictionary."""
    from trigrams import select_rand_key
    dic = {'key1': 1, 'key2': 2, 'key3': 3}
    assert select_rand_key(dic) in dic


def test_add_to_book_key():
    """Test that add_to_book adds a value to the book."""
    from trigrams import add_to_book
    words = 'a test'
    book = 'this is'
    assert add_to_book(book, words) == 'this is a test'


def test_add_to_empty_book():
    """Test that add_to_book adds the value to the book at a new sentence."""
    from trigrams import add_to_book
    words = 'this is'
    book = ''
    assert add_to_book(book, words) == 'this is'


def test_get_random_value():
    """Test that get_random_value gets a random value from a key."""
    from trigrams import get_random_value
    dic = {'key1': [1, 2, 3], 'key2': [2, 4, 6], 'key3': [3, 6, 9]}
    key = 'key3'
    assert get_random_value(dic, key) in dic[key]
