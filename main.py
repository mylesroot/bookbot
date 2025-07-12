import sys
from stats import get_num_words, get_character_counts, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
        return book_text

def create_report(sorted_dict, word_count, filepath):

    cleaned_dict_output = ""

    for item in sorted_dict:

        character = item['char']

        count = item['count']

        cleaned_dict_output = cleaned_dict_output + f"{character}: {count}\n"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}..")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(cleaned_dict_output)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        book_text = get_book_text(filepath)
        word_count = get_num_words(book_text)
        character_count = get_character_counts(book_text)
        sorted_list = sort_dictionary(character_count)
        print(create_report(sorted_list, word_count, filepath))


main()
