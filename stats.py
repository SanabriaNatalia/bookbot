import string

def count_words(contents : str):
    words = contents.split()
    return len(words)

def count_all_characters(contents : str):
    custom_chars = "æâêëô"
    lowercase_and_special = string.ascii_lowercase + custom_chars
    #print(lowercase_and_special)
    response = []

    for char in lowercase_and_special:
        item = {}
        item["char"] = char
        item["num"] = count_specific_character(contents, char)
        response.append(item)

    return response

def count_specific_character(sentence : str, character : str):
    return sentence.lower().count(character)

def sort_on(items):
    return items["num"]

def sort_dictionary(count_dict : dict[str:int]):
    count_dict.sort(reverse=True, key=sort_on)
    return count_dict

