def preprocess_words(file_path):
    """
    Preprocess the words from the file to create a dictionary
    where the keys are sorted words and values are lists of anagrams.
    
    Args:
        file_path (str): The path to the WORD.lst file.
        
    Returns:
        dict: A dictionary of anagram lists.
    """
    anagrams_dict = {}
    
    with open(file_path) as file:
        for word in file:
            word = word.rstrip().lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)
            else:
                anagrams_dict[sorted_word] = [word]
    
    return anagrams_dict

def anagrams(word, anagrams_dict):
    """
    Returns a list of anagrams of the given word using the preprocessed dictionary.

    Args:
        word (str): The word for which to find anagrams.
        anagrams_dict (dict): The dictionary of preprocessed anagrams.

    Returns:
        list: A list of anagrams of the given word.
    """
    sorted_word = ''.join(sorted(word.lower()))
    return anagrams_dict.get(sorted_word, [])

if __name__ == "__main__":
    anagrams_dict = preprocess_words('WORD.lst')

    print(anagrams("train", anagrams_dict))
    print('--')
    print(anagrams('drive', anagrams_dict))
    print('--')
    print(anagrams('python', anagrams_dict))

    query = input("Enter a word to find its anagrams: ")
  
    result = anagrams(query, anagrams_dict)
    if result:
        print(f"Anagrams for '{query }': {result}")
    else:
        print(f"No anagrams found for '{query }'")
    print('--')
