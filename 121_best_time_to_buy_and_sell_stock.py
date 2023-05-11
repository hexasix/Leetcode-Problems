class Solution:
    def maxProfit(prices: list[int]) -> int:
        answer = 0
        current_min = prices[0]
        lp = 0
        rp = 1
        while rp < len(prices):
            if (prices[rp]-prices[lp]) > answer:
                answer = prices[rp]-prices[lp]
            if prices[rp]<current_min:
                current_min = prices[rp]
                prices[lp] = current_min
            rp+=1
            continue
        return answer
    
prices = [7,6,4,3,1]
print(Solution.maxProfit(prices))