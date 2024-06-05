class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        mlist = []

        for i in range(len(rectangles)):
            mlist.append((min(rectangles[i][0], rectangles[i][1])))

        big = max(mlist)
        c = 0 
        for i in mlist:
            if i == big:
                c+=1
        
        return c
        