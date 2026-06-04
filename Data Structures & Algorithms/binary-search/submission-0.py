class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low + 1) // 2
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid
        if nums[low] == target:
            return low
        else:
            return -1