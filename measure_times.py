import time
from anagrams import anagrams as anagrams1
from anagrams_scalable import anagrams as anagrams2
from anagrams_scalable import preprocess_words
from anagrams_one_load import anagrams as anagrams3

def measure_time_approach_1(queries):
    """
    Measure the time of approach 1: Loading the file in each query.
    """
    query_times = []
    for query in queries:
        start_time = time.time()
        anagrams1(query)
        query_times.append(time.time() - start_time)
    
    print("Approach 1 (anagrams.py):")
    for i, query_time in enumerate(query_times):
        print(f"Query time {i+1}: {query_time:.6f} seconds")

def measure_time_approach_2(queries):
    """
    Measure the time of approach 2: Loading the file once and using the preprocessed dictionary.
    """
    # Measure the time of preprocessing the words
    start_time = time.time()
    anagrams_dict = preprocess_words('WORD.lst')
    preprocess_time = time.time() - start_time

    # Measure the time of multiple queries
    query_times = []
    for query in queries:
        start_time = time.time()
        anagrams2(query, anagrams_dict)
        query_times.append(time.time() - start_time)

    print("Approach 2 (anagrams_scalable.py):")
    print(f"Processing time: {preprocess_time:.6f} seconds")
    for i, query_time in enumerate(query_times):
        print(f"Query time {i+1}: {query_time:.6f} seconds")

def measure_time_approach_3(queries):
    """
    Measure the time of approach 3: Loading the file once before multiple queries.
    """
    # Measure the time of loading the words
    start_time = time.time()
    with open('WORD.lst') as file:
        words = [w.rstrip().lower() for w in file]
    load_time = time.time() - start_time

    # Measure the time of multiple queries
    query_times = []
    for query in queries:
        start_time = time.time()
        anagrams3(query, words)
        query_times.append(time.time() - start_time)

    print("Approach 3 (anagrams_one_load.py):")
    print(f"Load time: {load_time:.6f} seconds")
    for i, query_time in enumerate(query_times):
        print(f"Query time {i+1}: {query_time:.6f} seconds")

if __name__ == "__main__":
    queries = ["train", "drive", "python"]
    
    measure_time_approach_1(queries)
    print('--')
    measure_time_approach_2(queries)
    print('--')
    measure_time_approach_3(queries)