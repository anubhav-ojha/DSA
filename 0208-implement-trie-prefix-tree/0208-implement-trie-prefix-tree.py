
class Trie:
    class TrieNode:
        def __init__(self):
            self.arr = [None] * 26
            self.end = False
    
    def __init__(self):
        self.root = self.TrieNode()
    
    def insert(self, s: str) -> None:
        curr = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if curr.arr[idx] is None:
                curr.arr[idx] = self.TrieNode()
            curr = curr.arr[idx]
        curr.end = True
    
    def search(self, s: str) -> bool:
        curr = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if curr.arr[idx] is None:
                return False
            curr = curr.arr[idx]
        return curr.end
    
    def startsWith(self, s: str) -> bool:
        curr = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if curr.arr[idx] is None:
                return False
            curr = curr.arr[idx]
        return True