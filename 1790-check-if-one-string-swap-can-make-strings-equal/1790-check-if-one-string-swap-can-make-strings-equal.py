class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cdiff = 0
        diffs = []
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cdiff += 1
                diffs.append([s1[i], s2[i]])

        if cdiff != 2:
            return False
        
        for i in diffs:
            if diffs[0][0] == diffs[1][1] and diffs[0][1] == diffs[1][0]:
                return True
                
            