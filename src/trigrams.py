"""a trigram algorithm that generates text using a book-sized file as input."""
import io

def main(file_path, num_words):
    data = input_file(file_path)
    print(data)


def input_file(path):
    file = io.open(path)
    data = file.read()
    return data


if __name__ == '__main__':
    main('sample.txt', 200)
