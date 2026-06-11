class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        
        for i, number in enumerate(nums):
            index[number] = i
        
        for i, number in enumerate(nums):
            diff = target - number
            if diff in index and index[diff] != i:
                return [i, index[diff]]
        return []

