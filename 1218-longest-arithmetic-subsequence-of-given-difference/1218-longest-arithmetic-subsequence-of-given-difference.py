class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}  # Stores the maximum length at each index
        
        ans = 1  # Initialize with the minimum length of 1
        
        for i in range(n):
            num = arr[i]
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
            
            ans = max(ans, dp[num])
        
        return ans
        