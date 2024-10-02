class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        #first I will create set of sorted arr
        unique_sorted = sorted(set(arr))

        #map the value of each num in array accourding to its accourance
        rank_dict = {num: rank + 1 for rank, num in enumerate(unique_sorted)}

        return [rank_dict[num] for num in arr]
        