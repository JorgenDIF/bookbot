from stats import count_words, count_chars, the_one
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = count_words(book_text)
    char_counts = count_chars(book_text)
    sorted_chars = the_one(char_counts)

    print(f"Found {num_words} total words\n")

    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")


if __name__ == "__main__":
    main()
