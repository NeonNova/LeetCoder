class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        bigCount = [0]*26
        smolCount = [0]*26

        for i in range(len(s1)):
            bigCount[ord(s1[i]) - 97] += 1
            smolCount[ord(s2[i]) - 97] += 1

        matches = 0 

        for i in range(26):
            matches += (1 if bigCount[i] == smolCount[i] else 0)

        if matches == 26:
            return True

        l = 0 
        for r in range(len(s1), len(s2)):
            index = ord(s2[r]) - 97
            smolCount[index] += 1
            if bigCount[index] == smolCount[index]:
                matches += 1
            elif bigCount[index] + 1 == smolCount[index]:
                matches -= 1

            index = ord(s2[l]) - 97
            smolCount[index] -= 1
            if bigCount[index] == smolCount[index]:
                matches += 1
            elif bigCount[index] - 1 == smolCount[index]:
                matches -= 1
            l += 1

            if matches == 26:
                return True

        return False