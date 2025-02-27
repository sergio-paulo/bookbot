from stats import get_num_words, get_char_count

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
    
def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    char_dict = get_char_count(book_text)
    print(char_dict)
main()