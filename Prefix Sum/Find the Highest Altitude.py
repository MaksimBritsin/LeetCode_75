class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total_heigh = score = 0
        for i in gain:
            score += i
            total_heigh = max(total_heigh, score)
        return total_heigh