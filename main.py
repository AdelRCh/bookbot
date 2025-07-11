import sys
from stats import get_num_words, get_char_stats, sort_char_stats

def get_book_text(path_to_file):
    file_contents = ''
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
    except:
        print("File does not exist.")
    return file_contents

def print_report(fname, nb_words, sortedstats):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fname}")
    print("----------- Word Count ----------")
    print(f"Found {nb_words} total words")
    print("--------- Character Count -------")

    for item in sortedstats:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

def main():

    #No book title supplied
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_addr=sys.argv[1]

    my_text=get_book_text(book_addr)
    nb_words = get_num_words(my_text)
    chr_stats = get_char_stats(my_text)
    sorted_stats = sort_char_stats(chr_stats)
    print_report(book_addr,nb_words,sorted_stats)

    return 0

main()
