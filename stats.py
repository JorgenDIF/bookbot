def count_words(book):
    words = len(book.split())
    return words


def count_chars(book):
    new_book = book.lower()
    dict_book = {}
    for char in new_book:
        dict_book[char] = dict_book.get(char, 0) + 1

    return dict_book


def the_one(dict):
    new_list = []
    for key, value in dict.items():
        new_list.append({"char": key, "count": value})
    newer_list = sorted(new_list, key=lambda d: d["count"],  reverse=True)
    
    return newer_list
