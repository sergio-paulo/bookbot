from stats import get_num_words, get_char_count, get_list_chars_dicts
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return  sys.exit(1)
       
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_dict = get_char_count(book_text)
    list_char_dicts = get_list_chars_dicts(char_dict)
    
    # prints report
    print("============ BOOKBOT ============")
    print(f"Analizing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in list_char_dicts:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['count']}")
    print("============= END ===============")
    

main()