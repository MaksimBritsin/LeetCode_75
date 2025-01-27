class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_place = (i == 0) or (flowerbed[i-1] == 0)
                right_place = (i == len(flowerbed) -1 ) or (flowerbed[i+1] == 0)
                if right_place and left_place:
                    flowerbed[i] = 1
                    count += 1
        return count>= n