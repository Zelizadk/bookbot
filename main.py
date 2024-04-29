def word_count(Book):
    letters = {}
    lower_book = Book.lower()
    for letter in lower_book:
        if letter in letters:
            letters[letter] +=1
        else:
            letters[letter] = 1
    return letters

def letter_sort(let_dict):
    for letter in let_dict:
        if letter.isalpha() == True:
            print(letter)

def main():
    out = 0
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            out +=1
        
    print(f"{out} words found in the decument")
    letter_sort(word_count(file_contents))
            
    

main()