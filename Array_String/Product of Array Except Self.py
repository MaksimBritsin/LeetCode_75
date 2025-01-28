class Solution:
    def productExceptSelf(self, nums):
        list_length = len(nums)
        new_list = [1] * list_length
        k = 1
        for i in range(list_length):
            new_list[i] = k
            k *= nums[i]

        k = 1
        for i in range(list_length - 1, -1, -1):
            new_list[i] *= k
            k *= nums[i]

        return new_list