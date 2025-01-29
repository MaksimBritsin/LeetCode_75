import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        max_1, max_2 = sys.maxsize, sys.maxsize

        for i in nums:
            if i <= max_1:
                max_1 = i
            elif i <= max_2:
                max_2 = i
            else:
                return True
        return False