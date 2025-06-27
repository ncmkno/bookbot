def get_num_words(text):
    return len(text.split()) 

def get_char_counts(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts 

def get_sorted_char_counts(char_counts):
    # Create a list of dictionaries for each character and its count
    char_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    # Sort the list by count descending
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list 