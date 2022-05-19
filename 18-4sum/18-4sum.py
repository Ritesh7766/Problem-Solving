class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        res, n = [], len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, n):
                if j > (i + 1) and nums[j] == nums[j - 1]: continue
                left, right = j + 1, n - 1
                while left < right:
                    sm = nums[i] + nums[j] + nums[left] + nums[right]
                    if sm == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                    elif sm > target: right -= 1
                    else: left += 1
        return res