class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j-i)
        #         res = max(area, res)
        # return res

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(area, res)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res