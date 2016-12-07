"""a trigram algorithm that generates text using a book-sized file as input."""
import io

def main(file_path, num_words):
    data = input_file(file_path)
    sentences = split_data(data)
    print(sentences)

def input_file(path):
    file = io.open(path)
    data = file.read()
    return data


def split_data(data):
    sentences = data.split('.')
    return sentences


if __name__ == '__main__':
    main('sample.txt', 200)
