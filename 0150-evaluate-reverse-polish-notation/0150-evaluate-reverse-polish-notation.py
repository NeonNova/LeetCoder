class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def maths(a,b,o):
            if o == '+':
                return a+b
            elif o =='-':
                return a-b
            elif o =='*':
                return a*b
            elif o == '/':
                return int(a/b)

        stack = []
        ops = ['+','-','/','*']

        

        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                res = maths(a,b,i)
                stack.append(res)

        if len(stack) == 1:
            return stack[0]
        return res



        