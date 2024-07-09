class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(','{','[']
        closes = [')','}',']']
        for i in s:
            if i in opens:
                stack.append(i)
            elif i in closes:
                if stack and opens.index(stack[-1]) == closes.index(i):
                    stack.pop()
                else:
                    return False
        
        if len(stack)>0:
            return False
        return True
        