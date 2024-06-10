class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ideal = sorted(heights)  # Create a sorted copy of the heights list
        ctwrong = 0
        for i in range(len(heights)):
            if heights[i] != ideal[i]:
                ctwrong += 1
        return ctwrong