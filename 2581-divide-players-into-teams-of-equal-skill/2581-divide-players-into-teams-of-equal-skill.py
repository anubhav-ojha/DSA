class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = 0
        if len(skill)%2 != 0 :
            return -1 
        skill.sort()
        left, right = 0, len(skill)-1
        targetSumm = skill[left] + skill[right]
        while left < right:
            currentSum = skill[left] + skill[right]
            if currentSum != targetSumm:
                return -1
            chemistry += skill[left] * skill[right] 
            right -= 1
            left += 1      
                
        return chemistry


        