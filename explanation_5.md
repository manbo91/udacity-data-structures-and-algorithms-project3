# Problem 5: Autocomplete with Tries

## Complexity Analysis

- Time complexity: 

    `Trie.insert(), Trie.find()`

    Above methods, each character will be visited. So the time
    complexity is O(n).

    `TrieNode.suffixes()`

    Above method, In the worst case, it is O(n) by visiting every
    character in a Trie. (n == all characters of Trie)

- Space complexity: `O(nc)`.

    In the worst case, every word has a differnt letter order.
    So the number of all characters is O(nc). (n = words, c = characters)
