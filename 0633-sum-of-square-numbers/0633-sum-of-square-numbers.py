import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Define the limit as the square root of c
        limit = math.isqrt(c)

        # Initialize two pointers
        low, high = 0, limit

        while low <= high:
            sum_of_squares = low * low + high * high
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                low += 1
            else:
                high -= 1

        return False
