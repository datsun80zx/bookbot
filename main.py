def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict, num_chars = count_char(text)
    chars_sorted = dict_to_list(char_dict)

    print(f"--- Begin the report of {book_path} ---")
    print(f"There are {word_count} words and {num_chars} characters in the document")
    print()

    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]} times")

    print("--- End Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    words = text.split()
    unique_chars = {}
    char_count = 0
    for word in words:
        word1 = word.lower()
        for i in word1:
            char_count += 1
            if i in unique_chars:
                unique_chars[i] += 1
            else:
                unique_chars[i] = 1
    return unique_chars, char_count
    
    # below is how the solution from the course accomplished what my code above does. 
    # chars = {}
    # for c in text:
    #     lowered = c.lower()
    #     if lowered in chars:
    #         chars[lowered] += 1
    #     else:
    #         chars[lowered] = 1
    # return chars

def sort(dict):
    return dict["num"]

def dict_to_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort)
    return sorted_list


main()
