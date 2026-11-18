class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and pos[diff] != i:
                return [i, pos[diff]]
        return []