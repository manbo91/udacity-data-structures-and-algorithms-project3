class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        if char in self.children:
            return self.children[char]
        else:
            self.children[char] = TrieNode()
            return self.children[char]

    def suffixes(self, suffix=''):
        words = list()
        self.suffixes_recursive(self, suffix, words)
        return words

    def suffixes_recursive(self, node, suffix, words):
        if node.is_word == True:
            words.append(suffix)

        if len(node.children) == 0:
            return

        for (char, trieNode) in node.children.items():
            self.suffixes_recursive(trieNode, suffix + char, words)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.insert(char)

        node.is_word = True

    def find(self, prefix):
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None

        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')
