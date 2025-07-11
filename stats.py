def get_num_words(large_text):
    nb_words=0
    try:
        words = large_text.split()
        nb_words = len(words)
    except:
        print("We do not have a text file to process.")

    return nb_words

def get_char_stats(large_text):
    char_stats={}
    chars = set()

    for letter in large_text:
        if letter.lower() in chars:
            char_stats[letter.lower()] = char_stats[letter.lower()] + 1
        else:
            char_stats[letter.lower()] = 1
            chars.add(letter.lower())

    return char_stats

def sort_char_stats(char_dict):

    def sort_on(items):
        return items["num"]

    output = []
    for key, value in char_dict.items():
        output.append({"char":key, "num":value})
    output.sort(reverse=True, key=sort_on)
    return output
