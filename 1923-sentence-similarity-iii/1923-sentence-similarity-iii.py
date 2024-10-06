class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        words1 = sentence1.split()
        words2 = sentence2.split()

        if len(words1) < len(words2):
            words1, words2 = words2, words1

        i,j = 0, 0

        while i < len(words2) and words1[i] == words2[i] :
            i += 1

        while j < len(words2) and words1[len(words1) -1 - j] == words2[len(words2) - 1 - j]:
            j += 1

        return (i + j) >= len(words2)        

        