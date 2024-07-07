def are_anagrams(w1, w2):
    """
    Determines if two words are anagrams.

    Args:
        w1 (str): The first word.
        w2 (str): The second word.

    Returns:
        bool: True if the words are anagrams, False otherwise.
    """
    return sorted(w1) == sorted(w2)

def anagrams(word, words):
    """
    Returns a list of anagrams of the given word using the words
    from the WORD.LST file. The comparison is case-insensitive.

    Args:
        word (str): The word for which to find anagrams.
        words (list): The list of words from WORD.LST file.

    Returns:
        list: A list of anagrams of the given word.
    """
    # Convert the input word to lowercase
    word = word.lower()

    # Filter the list of words to find anagrams of the given word
    anagrams_list = [w for w in words if are_anagrams(word, w)]

    return anagrams_list

if __name__ == "__main__":
    # Read the file and store the words in a list
    with open('WORD.lst') as file:
        words = [w.rstrip().lower() for w in file]
    
    print(anagrams("train", words))
    print('--')
    print(anagrams('drive', words))
    print('--')
    print(anagrams('python', words))
    # User input
    print('--')
    user_word = input("Enter a word to find its anagrams: ")
    print(anagrams(user_word, words))
