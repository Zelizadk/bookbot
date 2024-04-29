def word_count(Book):
    letters = {}
    lower_book = Book.lower()
    for letter in lower_book:
        if letter in letters:
            letters[letter] +=1
        else:
            letters[letter] = 1
    return letters

def main():
    out = 0
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            out +=1
        
        print(word_count(file_contents))
    print(out)
            
    

main()