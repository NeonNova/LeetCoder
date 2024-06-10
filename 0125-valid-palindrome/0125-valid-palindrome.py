class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0
        end = len(s) - 1

        while st < end:
            #check for alnum and update accordingly
            while st < end and not s[st].isalnum():
                st += 1
            while st < end and not s[end].isalnum():
                end -= 1
            # Compare the characters in a case-insensitive manner
            if s[st].lower() != s[end].lower():
                return False
            
            st += 1
            end -= 1

        return True