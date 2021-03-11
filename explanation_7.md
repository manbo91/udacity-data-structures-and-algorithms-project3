# Problem 7: HTTPRouter using a Trie

## Complexity Analysis

- Time complexity: (n == len(split_path(path)))

    `Router.lookup(), RouterTrie.find()`: `O(n)`

    Above methods, In order of path will be visited. So the time
    complexity is O(n).

    `Router.split_path()`: `O(n)`

    The built-in split() has a time compleixty of O(n).

    `Router.insert(), RouteTrie.insert()`: `O(n)`

    The above methods also, In order of path will be visited and inserted.
    So the time complexity is O(n).

    `RouterTrieNode.insert()`: `O(1)`

- Space complexity: `O(n)`.

    In the worst case all paths are different because we have all paths
    separated by "/". So the space complexity is O(n).
