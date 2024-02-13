def get_book_text_from_file(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["count"]

def get_letter_count(text):
    letters = {}
    letters_list = []
    letters_sorted = {}
    lowered_text = text.lower()

    for letter in lowered_text:
        
        if letter in letters:
            letters[letter] += 1
        elif letter.isalpha():
            letters[letter] = 1

    for letter in letters:
        letter_dict = {"letter": letter, "count": letters[letter]}
        letters_list.append(letter_dict)

    letters_list.sort(reverse=True, key=sort_on)

    for letter_dict in letters_list:
        letters_sorted[letter_dict["letter"]] = letter_dict["count"]

    return letters_sorted

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text_from_file(file_path)
    
    word_count = get_word_count(book_text)
    letter_counts = get_letter_count(book_text)

    print(f'--- Begin report of {file_path} ---')
    print(f'{word_count} words found in the document')
    for letter in letter_counts:
        print(f"The '{letter}' character was found {letter_counts[letter]} times")

main()