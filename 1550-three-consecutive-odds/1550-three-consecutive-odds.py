class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if (arr[i] + arr[i+1] + arr[i+2])%2 == 1 and (arr[i] + arr[i+1])%2 == 0 and (arr[i+2] + arr[i+1])%2 == 0 and (arr[i] + arr[i+2])%2 == 0:
                return True
        return False
        