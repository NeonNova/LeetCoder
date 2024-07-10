class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i not in ["../", "./"]:
                stack.append(i)
            elif stack and i == "../":
                stack.pop()

        return len(stack)
            
        