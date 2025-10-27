from stats import count_words, count_all_characters, sort_dictionary
import sys

def get_book_text(filepath : str):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def build_report(filepath : str):
    contents = get_book_text(filepath)
    num_words = count_words(contents)
    character_count = count_all_characters(contents)
    sorted = sort_dictionary(character_count)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        print(item["char"]+": "+str(item["num"]))
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    build_report(sys.argv[1])

main()