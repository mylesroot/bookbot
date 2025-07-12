def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count


def get_character_counts(book_text):
    count_dict = {}
    for character in book_text:
        lower = character.lower()
        if lower not in count_dict:
            count_dict[lower] = 1
        else:
            count_dict[lower] += 1
    return count_dict

def sort_dictionary(unsorted_dict):

    dict_list = []

    for char, count in unsorted_dict.items():
        dict_list.append({'char': char, 'count': count})

    dict_list.sort(reverse=True, key=lambda x: x['count'])

    return dict_list
