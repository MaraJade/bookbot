#!/usr/bin/python3

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_num_chars(book_text):
    characters = {}
    for char in book_text:
        c = char.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters


def sort_on(dict):
    return dict["num"]


def sort_dict(dictionary):
    char_list = []
    for key in dictionary:
        if key.isalpha():
            char_list.append({"char": key, "num": dictionary[key]})

    return sorted(char_list, key=lambda x: x['num'], reverse=True)


def main():

    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)

    num_words = get_num_words(book_contents)

    num_chars = get_num_chars(book_contents)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")

    sorted_chars = sort_dict(num_chars)
    for pair in sorted_chars:
        print(f"The '{pair['char']}' character was found {pair['num']} times")

    print("--- End report ---")


main()
