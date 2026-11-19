class Solution:
    def isPalindrome(self, s: str) -> bool:
        # res = ""

        # for char in s:
        #     if char.isalnum():
        #         res += char.lower()

        # return res == res[::-1]
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True





