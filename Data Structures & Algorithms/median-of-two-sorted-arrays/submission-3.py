class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        if n % 2 == 1:
            return nums3[n//2]
        else:
            median = nums3[n//2] + nums3[n//2 - 1]
            return median / 2