class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ')':
                stack.append(char)  # Push characters to the stack until we hit a ')'
            else:
                to_reverse = []
                # Pop characters from the stack until we hit a '('
                while stack[-1] != '(':
                    to_reverse.append(stack.pop())
                stack.pop()  
                stack.extend(to_reverse)
        
        return ''.join(stack)
