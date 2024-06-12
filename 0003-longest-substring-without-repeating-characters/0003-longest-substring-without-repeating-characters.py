class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        windowhash = []
        res = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in windowhash:
                while s[right] in windowhash:
                    windowhash.remove(s[left])
                    left += 1
            windowhash.append(s[right])
            res = max(res, right - left + 1)
        
        return res
