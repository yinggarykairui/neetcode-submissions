class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        upTo = 1
        for i in range(n):
            output[i] = upTo
            upTo *= nums[i]

        after = 1
        for i in reversed(range(n)):
            output[i] *= after
            after *= nums[i]
        return output