def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in char_dict:
            char_dict[char_lower] = 1
        else:
            char_dict[char_lower] += 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def get_list_chars_dicts(char_dict):
    list_chars_dicts = []
    for key, value in char_dict.items():
        list_chars_dicts.append({"char": key, "count": value})
    list_chars_dicts.sort(key=sort_on, reverse=True)
    return list_chars_dicts