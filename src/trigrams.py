"""a trigram algorithm that generates text using a book-sized file as input."""
import io
import string
import re
import random


def main(file_path, num_words):
    data = input_file(file_path)
    sentences = split_data(data)
    book_dic = build_dic(sentences)
    print(book_dic)
    book = build_book(book_dic, num_words)


def input_file(path):
    file = io.open(path)
    data = file.read()
    return data


def split_data(data):
    sentences = data.split('.')
    return sentences


def remove_punc(sentences):
    return re.sub('[%s]' % string.punctuation, ' ', sentences)


def build_dic(sentences):
    dic = {}
    for sentence in sentences:
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
    return sentence.split()


def add_to_dic(dic, key, value):
    if key in dic.keys():
        dic[key].append(value)
    else:
        dic[key] = [value]
    return dic


def build_book(dic, num_words):
    book = ''
    words_to_add = select_rand_key(dic)
    book = add_to_book(book, words_to_add)
    while len(book.split()) < num_words:
        new_word = get_random_value(dic, book.split()[-2:])
        book = add_to_book(book, new_word)
        if new_word == '.':
            book = add_to_book(book, select_rand_key(dic))


def select_rand_key(dic):
    random_key = random.sample(list(dic), 1)
    return random_key[0]


def add_to_book(book, words):
    if len(book) == 0:
        first_letter = words[0].upper()
        return first_letter + words[1:]
    return book + ' ' + words


def get_random_value(dic, key):
    random_value = random.choice(dic[key])
    return random_value

if __name__ == '__main__':
    main('sample.txt', 200)
