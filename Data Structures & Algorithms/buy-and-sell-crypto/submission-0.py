class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        result = 0

        while right < len(prices):
            if prices[right] <= prices[left]:
                left = right
                right = right + 1
            else:
                ws = left
                we = right
                while we < len(prices):
                    if prices[we] <= prices[ws]:
                        break
                    else:
                        result = max(result, prices[we]-prices[ws])
                        we +=1
                left = we
                right = we + 1
        return result
        