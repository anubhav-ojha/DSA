class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        revStr = set()
        count = 0
        for word in words:
            if word in revStr:
                count += 1
            else:
                revStr.add(word[::-1])
        return count        