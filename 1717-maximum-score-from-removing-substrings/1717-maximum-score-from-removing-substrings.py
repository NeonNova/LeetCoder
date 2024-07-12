class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ab, ba = 0, 0
        if x >= y:
            ab = 1
            ba = 2 
        else:
            ba = 1
            ab = 2

        stack = []
        score = 0 

        for i in range(len(s)):
            if ab == 1:
                if stack and stack[-1] == "a" and s[i] == "b":
                    stack.pop()
                    score += x
                elif stack and stack[-1] == "b" and s[i] == "a" and (i + 1 >= len(s) or s[i+1] != "b"):
                    stack.pop()
                    score += y
                else:
                    stack.append(s[i])

            elif ba == 1:
                if stack and stack[-1] == "b" and s[i] == "a":
                    stack.pop()
                    score += y
                elif stack and stack[-1] == "a" and s[i] == "b" and (i + 1 >= len(s) or s[i+1] != "a"):
                    stack.pop()
                    score += x
                else:
                    stack.append(s[i])

        return score