class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        st = 0
        end = len(height) - 1

        while st < end:
            # Calculate the area with the current st and end pointers
            newarea = (end - st) * min(height[st], height[end])
            # Update area if the new area is larger
            if newarea > area:
                area = newarea

            # Move the pointer pointing to the shorter line
            if height[st] < height[end]:
                st += 1
            else:
                end -= 1
        
        return area