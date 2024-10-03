def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    word_count = count_words(text)
    chars_dict = count_characters(text)
    sorted_chars = sorted(chars_dict.items(),key=lambda item: item[1], reverse=True)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    
def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text:
        letter = char.lower()
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

def book_text(path):
    with open(path) as f:
        return f.read()

main()
