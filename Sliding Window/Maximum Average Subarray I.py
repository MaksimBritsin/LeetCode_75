import sys
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = total_sum = sum(nums[:k])
        for i in range(k, len(nums)):
                total_sum += nums[i] - nums[i-k]
                max_sum = max(total_sum, max_sum)
        return float(max_sum / k) 
                