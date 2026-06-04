class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        numsSet = set(nums)

        for num in numsSet:
            if num - 1 not in numsSet:
                length = 1
                temp = num
                while temp + 1 in numsSet:
                    length += 1
                    temp += 1
                maxLength = max(length, maxLength)
        return maxLength
