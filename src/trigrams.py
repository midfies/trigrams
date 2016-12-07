"""a trigram algorithm that generates text using a book-sized file as input."""
import io
import string
import re


def main(file_path, num_words):
    data = input_file(file_path)
    sentences = split_data(data)
    book_dic = build_dic(sentences)
    print(sentences)


def input_file(path):
    file = io.open(path)
    data = file.read()
    return data


def split_data(data):
    sentences = data.split('.')
    return sentences


def remove_punc(sentences):
    return re.sub('[%s]' % string.punctuation, '', sentences)


def build_dic(sentences):
    for sentence in sentences:
        working_sentence = remove_punc(sentence)
        print(working_sentence)


if __name__ == '__main__':
    main('sample.txt', 200)
