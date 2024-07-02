## Implement the "annograms" function

Implement the `annograms` function that uses the `WORD.LST` file to return anagrams of the word given in the `word` parameter.

```python
def annograms(word):
    # Write your code here.
    words = [w.rstrip() for w in open('WORD.LST')]
    raise NotImplementedError

if __name__ == "__main__":
    print(annograms("train"))
    print('--')
    print(annograms('drive'))
    print('--')
    print(annograms('python'))