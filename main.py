def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    num_of_words = get_total_count(text)    
    character_count = get_character_dict(text)
    character_sorted_dict = get_sorted_list_of_dict(character_count)
    
    print(f"--- Begin report of {"books/frankenstein.txt"} ---")
    print(f"{num_of_words} words found in the document")
    print()
    
    for item in character_sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
def get_total_count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def get_sorted_list_of_dict(count_char_dict):
    sorted_dict_list = []
    for ch in count_char_dict:
        sorted_dict_list.append({"char": ch, "num": count_char_dict[ch]})
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list

def get_book_path(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_character_dict(text):
    counted_char_dict = {}
    lower_string = text.lower()
    
    for char in lower_string:
        if char in counted_char_dict:
            counted_char_dict[char] += 1
        else:
            counted_char_dict[char] = 1
    return counted_char_dict


main()