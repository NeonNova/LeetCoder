class Solution:
    def numWaterBottles(self, nBottles: int, nExchange: int) -> int:
        c = 0
        while nBottles >= nExchange:
            k = nBottles // nExchange
            c += nExchange*k
            nBottles -= nExchange*k

            nBottles += k


        return c+nBottles

        