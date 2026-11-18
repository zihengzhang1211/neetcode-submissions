class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             product *= nums[j]
        #     res.append(product)
        # return res
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        