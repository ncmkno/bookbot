"""Module for reading and displaying contents of the Frankenstein book file."""

def sort_on(dict):
    """Helper function to sort character dictionaries by count."""
    return dict["count"]

def main():
    """
    Read and display the contents of the Frankenstein book file.
    Opens the file from the books directory and prints its contents to stdout.
    """
    path_to_file = 'books/frankenstein.txt'

    with open(path_to_file, 'r', encoding='utf-8') as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")

    char_counts = count_characters(file_contents)
    print("\nCharacter counts:")
    for char_dict in char_counts:
        print(f"'{char_dict['char']}'\n{char_dict['count']}")
    
    print("--- End report ---")

def count_words(text):
    """Counts the number of words in a given string."""
    words = text.split()  # Split text by whitespace into words
    return len(words)

def count_characters(text):
    """Counts the frequency of each character in a given string."""
    text = text.lower()
    char_counts = {}

    # Only count alphabetic characters
    for char in text:
        if char.isalpha():  # Remove space condition
            char_counts[char] = char_counts.get(char, 0) + 1

    # Convert to list of dictionaries
    char_list = [{"char": char, "count": count} for char, count in char_counts.items()]
    # Sort by count in descending order
    char_list.sort(reverse=True, key=sort_on)
    return char_list

if __name__ == "__main__":
    main()
