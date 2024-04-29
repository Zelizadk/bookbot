def main():
    out = 0
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            out +=1
    print(out)
            
    

main()