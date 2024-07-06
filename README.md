# Exercise 1

This project contains a function `anagrams` that returns a list of anagrams of a given word using the words from the `WORD.lst` file.

## How to Run

1. Run the `anagrams` function:
    ```
    python anagrams.py
    ```

2. Enter a word when prompted to find its anagrams:
    ```
    Enter a word to find its anagrams: <your_word>
    ```

3. Run the tests:
    ```
    python -m unittest test_anagrams.py
    ```

## Example Usage

When you run the `anagrams.py` script, it will display the anagrams of the words "train", "drive", and "python". It will then prompt you to enter a word to find its anagrams.


# Exercise 1  - Refined 

The refined version anagrams_scalable.py addresses the question of how the anagrams.py algorithm could be improved in terms of scalability (i.e., many users querying the algorithm simultaneously).

For more information, see the file Complexity_Analysis.md


## How to Run

1. Run the `anagrams_scalable` function:
    ```
    python anagrams_scalable.py
    ```

2. Enter a word when prompted to find its anagrams:
    ```
    Enter a word to find its anagrams: <your_word>
    ```

3. Run the tests:
    ```
    python -m unittest test_anagrams_scalable.py
    ```

## Example Usage

When you run the `anagrams_scalable.py` script, it will prompt you to enter a word to find its anagrams and return the result.

