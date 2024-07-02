def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    list = count_words(text)
    print(f"{list} words found in document")  

def get_book_text(path):
    with open(path) as f: 
        return f.read()

def count_words(text):
    list = text.split()
    return len(list)
        

main()