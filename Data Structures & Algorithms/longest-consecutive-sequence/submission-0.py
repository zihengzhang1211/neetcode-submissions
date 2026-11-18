class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # res = 0
        # for num in nums:
        #     length = 1
        #     cur = num

        #     while cur + 1 in nums:
        #         cur += 1
        #         length += 1
            
        #     res = max(res, length)
        # return res

        # if not nums:
        #     return 0

        # nums.sort()

        # res = 1
        # length = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue

        #     if nums[i] == nums[i - 1] + 1:
        #         length += 1
        #     else:
        #         length = 1

        #     res = max(res, length)

        # return res
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while (num + length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest






