class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums): #enumerate nums makes i index, a the value
            if a > 0: #if a >0, then no combination of 3 will work
                break

            if i > 0 and a == nums[i-1]: #if the index is more than 0, and i is equal to the first term (aside for the left pointer)
                continue
            
            l, r = i + 1, len(nums) - 1 #classic two point with left and right
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: #too big
                    r -= 1
                elif threeSum < 0: #too small
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) #append the values
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: #ensures that no duplicate left variables. No need to check for right even though there may be duplicates because left variable will be different, so the outcome won't be the same
                        l += 1
        return res