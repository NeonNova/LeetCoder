class Solution:
    def passThePillow(self, n: int, t: int) -> int:
        return (t%(k:=n-1),k-t%k)[t//k%2]+1