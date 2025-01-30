def main():
    path_to_book = "books/frankenstein.txt"
    with open(path_to_book) as f:
        book = f.read()
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{count_words(book)} words found in the document")
    print_report(count_characters(book))
    print("--- End report ---")



def count_characters(book):
    character_count = {}
    for character in book:
        if character.lower() not in character_count:
            character_count[character.lower()] = 1
        else:
            character_count[character.lower()] += 1
    return character_count


def print_report(character_count_dic):
    sorted_character = sorted(character_count_dic.items(),key=lambda x:x[1], reverse=True) 
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for character in dict(sorted_character):
        if character in alphabet_list:
            print(f"The '{character}' character was found {character_count_dic[character]} times")

def count_words(book):
   words = book.split()
   return len(words)




main()
