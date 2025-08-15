import sys
from stats import get_num_words, get_char_frequencies, get_sorted_alpha_chars

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)


def get_book_text(file_path):
    """Reads and returns the contents of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."

def main():
    """Main function to print the word count and sorted alphabetical character frequencies of frankenstein.txt."""
    file_path =  sys.argv[1]
    result = get_book_text(file_path)
    if result.startswith("Error:"):
        print(result)
        return
    
    num_words = get_num_words(result)
    print("===============BOOKBOT=================")
    print(f"Analyzing book found at {file_path}...")
    print("--------------Word Count---------------")
    print(f"Found {num_words} total words")
    
    char_freq = get_char_frequencies(result)
    sorted_alpha_chars = get_sorted_alpha_chars(char_freq)
    
    print("------------Character Count-------------")
    for item in sorted_alpha_chars:
        print(f"{item['char']}: {item['num']}")
    print("================END=====================")
if __name__ == "__main__":
    main()
