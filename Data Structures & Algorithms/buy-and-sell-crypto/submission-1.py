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
                #ws = left
                #we = right
                while right < len(prices):
                    if prices[right] <= prices[left]:
                        break
                    else:
                        result = max(result, prices[right]-prices[left])
                        right +=1
                left = right
                right = right + 1
        return result
        