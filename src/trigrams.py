"""a trigram algorithm that generates text using a book-sized file as input."""
import io

def main(file_path, num_words):
    print('hi')
    input_file(file_path)


def input_file(path):
    file = io.open(path)
    print(file)


if __name__ == '__main__':
    main('sample.txt', 200)
