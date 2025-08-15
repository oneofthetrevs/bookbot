def get_num_words(text):
    """Returns the number of words in the given text string."""
    if text.startswith("Error:"):
        return 0
    words = text.split()
    return len(words)

def get_char_frequencies(text):
    """Returns a dictionary with the frequency of each character in the text (lowercase)."""
    if text.startswith("Error:"):
        return {}
    char_freq = {}
    for char in text.lower():
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq
def get_sorted_alpha_chars(char_freq):
    """Returns a list of dictionaries with alphabetical characters and their counts, sorted by count descending."""
    alpha_chars = [
        {"char": char, "num": count}
        for char, count in char_freq.items()
        if char.isalpha()
    ]
    alpha_chars.sort(key=lambda x: x["num"], reverse=True)
    return alpha_chars
