"""a trigram algorithm that generates text using a book-sized file as input."""
import io
import string
import re
import random
import sys


def main(file_path, num_words):
    '''Call the primary functions of this module.'''
    num_words = int(num_words)
    data = input_file(file_path)
    sentences = split_data(data)
    book_dic = build_dic(sentences)
    book = build_book(book_dic, num_words)
    first_letter_of_book = book[0].upper()
    book = first_letter_of_book + book[1:]
    # book = capitalize_sentences(book)

    print(book)


def input_file(path):
    '''Open and read a given file.'''
    file = io.open(path)
    data = file.read()
    return data


def split_data(data):
    '''Split file into individual sentences.'''
    sentences = data.split('.')
    return sentences


def remove_punc(sentences):
    '''Remove punctuation from the sentences.'''
    return re.sub('[%s]' % string.punctuation, ' ', sentences)


def build_dic(sentences):
    '''Call funtions that build dictionary.'''
    dic = {}
    for sentence in sentences:
        print
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


def split_words(sentence):
    '''Split sentences into lists containing individual words.'''
    return sentence.split()


def add_to_dic(dic, key, value):
    '''Add two word keys and one word values to the dictionary.'''
    if key in dic.keys():
        dic[key].append(value)
    else:
        dic[key] = [value]
    return dic


def build_book(dic, num_words):
    '''Add the generated sentences to the book.'''
    book = ''
    words_to_add = select_rand_key(dic)
    book = add_to_book(book, words_to_add)
    while len(book.split()) < num_words:
        last_two = book.split()[-2:]
        last_two_string = last_two[0] + ' ' + last_two[1]
        new_word = get_random_value(dic, last_two_string)
        book = add_to_book(book, new_word)
        if new_word == '.':
            book = add_to_book(book, select_rand_key(dic))
    return book


def select_rand_key(dic):
    '''Select a random key from the dictionary.'''
    random_key = random.sample(list(dic), 1)
    return random_key[0]


def add_to_book(book, words):
    '''Add generated words to the book.'''
    if len(book) == 0:
        return words
    if words == '.':
        return book + words
    return book + ' ' + words


def get_random_value(dic, key):
    '''Get random value from a key.'''
    random_value = random.choice(dic[key])
    return random_value

# def capitalize_sentences(book):
#     updated_book = ''
#     sentences = book.split('.')
#     for sentence in sentences:
#         sentence_start = sentence[1].upper()
#         sentence = sentence_start + sentence[2:] + '. '
#         updated_book  += sentence
#     return updated_book


if __name__ == '__main__':
    print(sys.argv[1], sys.argv[2])
    main(sys.argv[1], sys.argv[2])
