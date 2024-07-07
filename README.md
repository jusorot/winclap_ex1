# Exercise 1

This project contains three approaches for a function `anagrams` that returns a list of anagrams of a given word using the words from the `WORD.lst` file.

## Approach 1 - anagrams.py

### How to Run

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

### Example Usage

When you run the `anagrams.py` script, it will display the anagrams of the words "train", "drive", and "python". It will then prompt you to enter a word to find its anagrams.


## Approach 2 - anagrams_scalable.py

The refined version anagrams_scalable.py addresses the question of how the anagrams.py algorithm could be improved in terms of scalability (i.e., many users querying the algorithm simultaneously).

### How to Run

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

### Example Usage

When you run the `anagrams_scalable.py` script, it will display the anagrams of the words "train", "drive", and "python". It will then prompt you to enter a word to find its anagrams.

## Approach 3- anagrams_one_load.py

This new approach was introduced to compare execution times. It represents an intermediate solution simpler than the dictionary preprocessing approach and more refined than the initial approach.

### How to Run

1. Run the `anagrams_one_load` function:
    ```
    python anagrams_one_load.py
    ```

2. Enter a word when prompted to find its anagrams:
    ```
    Enter a word to find its anagrams: <your_word>
    ```

3. Run the tests:
    ```
    python -m unittest test_anagrams_one_load.py
    ```

### Example Usage

When you run the `anagrams_one_load.py` script, it will display the anagrams of the words "train", "drive", and "python". It will then prompt you to enter a word to find its anagrams.

## Performance Comparison - measure_times.py

The script measure_times.py measures and compares the performance of the three approaches:

    anagrams.py: This is the initial approach that reads the WORD.lst file and filters anagrams on-the-fly for each query. It is straightforward but less efficient for multiple queries due to repeated file loading.

    anagrams_scalable.py: This approach preprocesses the WORD.lst file into a dictionary where keys are sorted words and values are lists of anagrams. This preprocessing step incurs an initial overhead but allows for fast query times, making it suitable for scenarios with many queries.

    anagrams_one_load.py: This new approach refines the initial approach by loading the WORD.lst file once at the beginning and reusing the list of words for all queries. This simple improvement effectively eliminates the overhead of repeated file loading observed in anagrams.py.

## How to Run measure_times.py

### How to Run

Run the `measure_times` function:
    ```python 
    measure_times.py
    ```

    The script will run several example queries and display the loading and query times for each approach.

### Example Output

The measure_times.py script will produce output similar to the following:

 ```yaml
Approach 1 (anagrams.py):
Query time 1: 0.192892 seconds
Query time 2: 0.176831 seconds
Query time 3: 0.197697 seconds
--
Approach 2 (anagrams_scalable.py):
Processing time: 0.315048 seconds
Query time 1: 0.000000 seconds   
Query time 2: 0.000000 seconds   
Query time 3: 0.000000 seconds   
--
Approach 3 (anagrams_one_load.py):
Load time: 0.066220 seconds   
Query time 1: 0.135337 seconds
Query time 2: 0.135494 seconds
Query time 3: 0.141099 seconds
 ```


 # Conclusion

    Approach 1 (anagrams.py) is the least efficient for multiple queries due to repeated file loading.
    Approach 2 (anagrams_scalable.py) preprocesses the file into a dictionary, resulting in fast query times but has an initial overhead.
    Approach 3 (anagrams_one_load.py) loads the file once and reuses the word list, reducing load time compared to Approach 1 but query times are significantly higher than Approach 2.

For scenarios with multiple queries, Approach 2 is the most efficient choice.

To explore a theoretical Big O analysis for each approach that corroborates these findings, refer to the "Complexity_Analysis" file.