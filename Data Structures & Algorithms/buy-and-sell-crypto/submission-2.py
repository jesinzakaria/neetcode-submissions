class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, l = 0, len(prices)
        right = left + 1
        result = 0

        while right < l:
            if prices[right] <= prices[left]:
                left = right
                right = right + 1
            else:
                #ws = left
                #we = right
                while right < l:
                    if prices[right] <= prices[left]:
                        break
                    else:
                        result = max(result, prices[right]-prices[left])
                        right +=1
                left = right
                right = right + 1
        return result
        