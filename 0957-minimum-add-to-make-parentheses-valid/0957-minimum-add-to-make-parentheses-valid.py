class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        countLeft, countRight = 0, 0

        for c in s:
            if c == "(":
                countLeft += 1
            elif c == ")" and countLeft > 0:
                countLeft -= 1
            else:
                countRight += 1    

            

        return abs(countLeft + countRight)            
        