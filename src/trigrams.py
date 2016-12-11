"""A trigram algorithm that generates text using a book-sized file as input."""
import string
import re
import random
import sys


def main(file_path, num_words):
    """Call the primary functions of this module."""
    data = input_file(file_path)
    sentences = split_data(data)
    book_dic = build_dic(sentences)
    book = build_book(book_dic, num_words)
    first_letter_of_book = book[0].upper()
    book = first_letter_of_book + book[1:]
    print(book)
    return book


def build_dic(sentences):
    """Call funtions that build dictionary."""
    dic = {}
    for sentence in sentences:
        if type(sentence[0]) is not 'int':
            first_letter = sentence[0].lower()
        sentence = first_letter + sentence[1:]
        working_sentence = remove_punc(sentence)
        word_array = split_words(working_sentence)
        for i in range(len(word_array) - 1):
            key_word = word_array[i] + ' ' + word_array[i + 1]
            if word_array[i + 1] is not word_array[-1]:
                value_word = word_array[i + 2]
            else:
                value_word = '.'
            dic = add_to_dic(dic, key_word, value_word)
    return dic


def build_book(dic, num_words):
    """Add the generated sentences to the book."""
    book = ''
    words_to_add = select_rand_key(dic)
    book = add_to_book(book, words_to_add)
    while len(book.split()) < num_words:
        last_two = ' '.join(book.split()[-2:])
        new_word = get_random_value(dic, last_two)
        book = add_to_book(book, new_word)
        if new_word == '.':
            book = add_to_book(book, select_rand_key(dic))
    return book


def input_file(path):
    """Open and read a given file."""
    with open(path) as f:
        data = f.read()
    return data


def split_data(data):
    """Split file into individual sentences."""
    sentences = data.split('.')
    return sentences


def remove_punc(sentences):
    """Remove punctuation from the sentences."""
    return re.sub('[%s]' % string.punctuation, ' ', sentences)


def split_words(sentence):
    """Split sentences into lists containing individual words."""
    return sentence.split()


def add_to_dic(dic, key, value):
    """Add two word keys and one word values to the dictionary."""
    dic.setdefault(key, [])
    dic[key].append(value)
    return dic


def select_rand_key(dic):
    """Select a random key from the dictionary."""
    return random.sample(list(dic), 1)[0]


def add_to_book(book, words):
    """Add generated words to the book."""
    if len(book) == 0:
        return words
    if words == '.':
        return book + words
    return ' '.join([book, words])


def get_random_value(dic, key):
    """Get random value from a key."""
    return random.choice(dic[key])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
