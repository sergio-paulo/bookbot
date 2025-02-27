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

