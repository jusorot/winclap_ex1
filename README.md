# Exercise 1

This project contains a function `anagrams` that returns a list of anagrams of a given word using the words from the `WORD.lst` file.

## How to Run

1. Activate the virtual environment:
    ```
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows
    ```

2. Run the `anagrams` function:
    ```
    python anagrams.py
    ```

3. Enter a word when prompted to find its anagrams:
    ```
    Enter a word to find its anagrams: <your_word>
    ```

4. Run the tests:
    ```
    python -m unittest test_anagrams.py
    ```

## Example Usage

When you run the `anagrams.py` script, it will display the anagrams of the words "train", "drive", and "python". It will then prompt you to enter a word to find its anagrams.
