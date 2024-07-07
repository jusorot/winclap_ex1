# Complexity Analysis

The concept of Big O in computer science is closely related to the scalability of algorithms. Big O describes the efficiency or time complexity of an algorithm in terms of the input size. It is used to analyze how the runtime or resource usage (such as memory) increases as the size of the data being processed grows.

In terms of scalability, an algorithm with a lower Big O notation (such as O(1) or O(log n)) is more efficient and scalable than one with a higher notation (such as O(n) or O(n^2)). Therefore, when selecting algorithms for applications that handle large volumes of data, it is crucial to consider the time complexity (Big O) to ensure that the system can handle the expected growth without significant performance degradation.

This is a complexity Analysis for algorithms: 
1. anagrams (Approach 1 - Non-Preprocessing Approach)
2. anagrams_scaled (Approach 2 - Preprocessing Aproach)

**Variables**

N : number of words in the list. For WORD.lst it is 173528 (≈ 200000)
m : average length of words. For WORD.lst it is ≈ 5
q: number of querys (scalability variable)


# Approach 1 (anagrams.py)

#### a. Reading and Storing Words:

All words from the file `WORD.lst` are read, containing N words, each with an average length of m characters. For each word, a strip operation and conversion to lowercase are performed, both operations being O(m). 

Therefore, the total time complexity for Reading and Storing Words is **O(N * m).**

#### b. Filtering Anagrams:

For each word in the list of N words, it is checked if it is an anagram of the given word. 

This involves calling the `are_anagrams` function that sorts both the given word and the word from the list, both operations having a complexity of O(m log m) due to the sorting operation. (Timsort) 

Since this is done for each of the q queries, N times, the total time is **O(N * m log m).**

### Total Complexity for anagrams.py:

To determine the overall complexity of the algorithm, we sum the time spent reading and storing words with the time spent verifying anagrams:

Per query: O(N * m) + O(N * m log m) = **O(N * m (1 + log m))** 

For q queries: **O( q * N * m (1 + log m))**

# Approach 2 (anagrams_scalable.py)

#### a. Initial Preprocessing:

Data Preprocessing and In-Memory Storage: 
Complexity of build the dictionary of anagrams (simplified): O(N * m log m).
The preprocess_words function reads all words from the file once and stores them in a dictionary named anagrams_dict, where keys are words sorted alphabetically and values are lists of words that are anagrams of those keys. 

This preprocessing process is **O(N * m log m).** 
However, this is performed only once at the beginning.

#### b. Individual Query:

The anagrams function takes a word, sorts it, and looks up the sorted word in the anagrams_dict dictionary.

Sort the input word: O(m log m).
Look up in the dictionary: O(1) 

Summing both parts, we get the complexity per query:

**O(m log m)** 


### Total Complexity for anagrams_scalable.py:

Preprocessing: O(N * m log m) (once).
Queries: O(q * m log m) 

Summing both parts, we get the total complexity:

 **O(N * m log m) + O(q * m log m)**


# Approach 3 (anagrams_one_load.py)

#### a. Reading and Storing Words:

All words from the file `WORD.lst` are read, containing N words, each with an average length of m characters. For each word, a strip operation and conversion to lowercase are performed, both operations being O(m).

Therefore, the total time complexity for Reading and Storing Words is **O(N * m).**

#### b. Filtering Anagrams:

For each word in the list of N words, it is checked if it is an anagram of the given word. 

This involves calling the `are_anagrams` function that sorts both the given word and the word from the list, both operations having a complexity of O(m log m) due to the sorting operation. (Timsort) 

Since this is done for each of the q queries, N times, the total time is **O(N * m log m).**

### Total Complexity for anagrams_one_load.py:

To determine the overall complexity of the algorithm, we sum the time spent reading and storing words with the time spent verifying anagrams:

Loading: O(N * m) 
Per query: O(N * m log m)
For q queries: O(N * m) + q * O(N * m log m)


## Complexity Summary

### Approach 1  
- Complexity per query: O(N * m (1 + log m))
- Total complexity for q queries: O(q * N * m (1 + log m))

### Approach 2
- Preprocessing: O(N * m log m) (once)
- Complexity per query: O(m log m)
- Total complexity for q queries: O(N * m log m) + O(q * m log m)

### Approach 3
- Loading: O(N * m) (once)
- Complexity per query: O(N * m log m)
- Total complexity for q queries: O(N * m) + O(q * N * m log m)


## Numerical Example

To illustrate better, let's consider an example with specific numbers:

    N: 200000 words in the file.
    m: 5 characters per word on average.
    q: 1000 user queries.

### Approach 1

- Complexity per query: N * m (1 + log m) = 200.000 × 5 (1 + log5) = 1.698.970
- Total complexity for q queries: q * N * m (1 + log m) = q * 1.698.970 = 1.698.970.004

### Approach 2

- Preprocessing: N * m log m = 200.000 × 5 x log5 = 698.970
- Complexity per query: m log m = 3,50
- Total complexity for q queries: N * m log m + q * m log m = 698.970 + q * 3,50 = 702.470

### Approach 3

- Loading: N * m = 200.000 x 5 = 1.000.000
- Complexity per query: N * m log m = 200.000 × 5 x log5 = 698.970
- Total complexity for q queries: N * m + q * N * m log m = 1.000.000 + q * 698.970 = 698.970.004


## Conclusion

These results illustrate that as the number of queries q increases, Approach 1 and 3 exhibit significantly higher total complexity compared to Approach 2. This suggests that for a substantial number of queries, Approach 1 might be preferable due to their lower complexity.

Note:

By definition, Big O considers the worst-case scenario of an algorithm's execution.


For further details and performance comparisons refer to the measure_times.py script where Approach 1, Approach 2 and Approach 3 are compared.

## Reference

- https://docs.python.org/3/howto/sorting.html#sortinghowto
- https://www.bigocheatsheet.com/

