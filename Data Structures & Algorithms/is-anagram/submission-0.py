class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # seen = {}
        # for char in s:
        #     seen[char] = seen.get(char, 0) + 1
        # for char in t:
        #     if char not in seen:
        #         return False
        #     seen[char] -= 1
        
        # for value in seen.values():
        #     if value != 0:
        #         return False
    
        # return True

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        