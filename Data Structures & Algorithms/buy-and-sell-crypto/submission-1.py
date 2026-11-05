class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mpro = 0

        for i in range(len(prices) - 1):
            cp = prices[i]
            for j in range(i + 1, len(prices)):
                sp = prices[j]
                pro = sp - cp
                mpro = max(pro,mpro)
        
        return mpro


        