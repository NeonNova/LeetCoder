class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        bigCount = defaultdict(int)
        smolCount = defaultdict(int)

        for i in range(len(s1)):
            bigCount[s1[i]] += 1
            smolCount[s2[i]] += 1

        matches = 0

        for char in bigCount:
            if bigCount[char] == smolCount[char]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(bigCount):
                return True

            right_char = s2[r]
            left_char = s2[l]

            smolCount[right_char] += 1
            if bigCount[right_char] == smolCount[right_char]:
                matches += 1
            elif bigCount[right_char] + 1 == smolCount[right_char]:
                matches -= 1

            smolCount[left_char] -= 1
            if bigCount[left_char] == smolCount[left_char]:
                matches += 1
            elif bigCount[left_char] - 1 == smolCount[left_char]:
                matches -= 1

            l += 1

        return matches == len(bigCount)