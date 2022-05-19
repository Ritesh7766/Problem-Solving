class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res, n = [], len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, n - 1
            while left < right:
                sm = nums[i] + nums[left] + nums[right]
                if sm == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
                elif sm > 0: right -= 1
                else: left += 1
        return res