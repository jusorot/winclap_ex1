# Complexity Analysis

The concept of Big O in computer science is closely related to the scalability of algorithms. Big O describes the efficiency or time complexity of an algorithm in terms of the input size. It is used to analyze how the runtime or resource usage (such as memory) increases as the size of the data being processed grows.

In terms of scalability, an algorithm with a lower Big O notation (such as O(1) or O(log n)) is more efficient and scalable than one with a higher notation (such as O(n) or O(n^2)). Therefore, when selecting algorithms for applications that handle large volumes of data, it is crucial to consider the time complexity (Big O) to ensure that the system can handle the expected growth without significant performance degradation.

This is a complexity Analysis for both algorithms: 
1. anagrams (Non-Preprocessing Approach)
2. anagrams_scaled (Preprocessing Aproach)

**Variables**

N : number of words in the list. For WORD.lst it is 173528 (≈ 200000)
m : average length of words. For WORD.lst it is ≈ 5
q: number of querys (scalability variable)


# Non-Preprocessing Approach (anagrams.py)

#### a. Reading and Storing Words:

All words from the file `WORD.lst` are read, containing N words, each with an average length of m characters. 

``` python
words = [w.rstrip().lower() for w in file]
```

For each word, a strip operation and conversion to lowercase are performed, both operations being O(m). 

Therefore, the total time complexity is **O(N * m).**

#### b. Filtering Anagrams:

For each word in the list of N words, it is checked if it is an anagram of the given word. 

``` python
anagrams_list = [w for w in words if are_anagrams(word, w)]
```

This involves calling the `are_anagrams` function that sorts both the given word and the word from the list, both operations having a complexity of O(m log m) due to the sorting operation. (Timsort) 

``` python
def are_anagrams(w1, w2):
    return sorted(w1) == sorted(w2)
```

Since this is done for each of the q queries, N times, the total time is **O(q * N * m log m).**

### Total Complexity for anagrams.py:

To determine the overall complexity of the algorithm, we sum the time spent reading and storing words with the time spent verifying anagrams:

O(N * m) + O(q * N * m log m)

We keep with the dominant term which is O(q * N * m log m), as it grows faster than O(N * m) as N, m, and q increase.

Considering the above points, the dominant complexity is:

**O(q * N * m log m)**


# Preprocessing Approach (anagrams_scalable.py)

#### a. Initial Preprocessing:

Data Preprocessing and In-Memory Storage: Construct the dictionary of anagrams: O(N * m log m).
The preprocess_words function reads all words from the file once and stores them in a dictionary named anagrams_dict, where keys are words sorted alphabetically and values are lists of words that are anagrams of those keys. 

This preprocessing process is **O(N * m log m).** However, this is performed only once at the beginning.

``` python
def preprocess_words(file_path):
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
``` 


#### b. Individual Query:

The anagrams function takes a word, sorts it, and looks up the sorted word in the anagrams_dict dictionary.

``` python
def anagrams(word, anagrams_dict):
    sorted_word = ''.join(sorted(word.lower()))
    return anagrams_dict.get(sorted_word, [])
``` 

Sort the input word: O(m log m).
Look up in the dictionary: O(1).

Summing both parts, we get the complexity per query:

**O(m log m)** 


### Total Complexity for anagrams_scalable.py:

Preprocessing: O(N * m log m) (once).
Queries: O(q * m log m) 

Summing both parts, we get the total complexity:

 **O(N * m log m) + O(q * m log m)**



## Complexity Summary

### Non-Preprocessing Approach
- Complexity per query: O(N * m log m)
- Total complexity for q queries: O(q * N * m log m)
- Considering m a constant (Drop constants): O(q * N)

### Preprocessing Approach
- Preprocessing: O(N * m log m) (once)
- Complexity per query: O(m log m)
- Total complexity for q queries: O(N * m log m) + O(q * m log m)
- Considering m a constant (Drop constants): O(N) + O(q)



## Numerical Example

To illustrate better, let's consider an example with specific numbers:

    N: 200000 words in the file.
    m: 5 characters per word on average.
    q: 1000 user queries.

### Without Preprocessing

For each query:

    File processing: O(200,000 × 5 log5) ≈ O(1,000,000 log5).
    For q queries: 1,000 × 1,000,000 log5 = 1,000,000,000 log5.


### With Preprocessing

Initial preprocessing:

    O(200,000 × 5 log⁡5) ≈ O(1,000,000 log5).

For each query:

    Dictionary lookup: O(5 log5).
    For n queries: 1,000 × 5 log⁡5 = 5,000 log5.

Total with preprocessing:

    O(1,000,000 log5) + O(5,000 log5) = 1,005,000 log5.


## Final Comparison

Without Preprocessing: **1,000,000,000 log5.**

With Preprocessing: **1,005,000 log5.**


## Conclusion

The preprocessing approach is more efficient in terms of total time, especially when there are a large number of queries, because the preprocessing cost is distributed, and individual queries are much faster.


## Reference

https://docs.python.org/3/howto/sorting.html#sortinghowto
https://www.bigocheatsheet.com/

