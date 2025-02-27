
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_num_words(text):
    return len(text.split())
    
def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    
main()