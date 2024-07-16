

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
    let_dict = dict(sorted(let_dict.items(), key=lambda item: item[1],reverse=True))
    for letter in let_dict:
        if letter.isalpha():
            print(f"the '{letter}' character was found {let_dict[letter]} times")

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
    print("--- End report ---")
            
    

main()