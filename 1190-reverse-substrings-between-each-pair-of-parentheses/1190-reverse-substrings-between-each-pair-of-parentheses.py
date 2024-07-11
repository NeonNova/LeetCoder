class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        torev = ""

        for i in s:
            torev=""
            if i != ')':
                stack.append(i)
            else:
                while stack[-1] != '(':
                    torev+=stack.pop()
                else:
                    stack.pop()
                stack.append(torev[::-1])
                
        
        return (stack[0][::-1])