class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        new_list = []
        for i in candies:
            new_list.append(i + extraCandies >= max_candies)
        return new_list