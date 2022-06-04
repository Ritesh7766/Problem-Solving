class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max, right_max = [0] * n, [0] * n
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        total = 0
        for i in range(n):
            water = min(right_max[i], left_max[i]) - height[i]
            if water > 0: total += water
        return total