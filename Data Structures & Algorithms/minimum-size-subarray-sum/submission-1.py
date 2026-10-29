class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, sum = 0, 0
        length = float("inf")
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                length = min(length, r-l+1)
                sum -= nums[l]
                l += 1
        return 0 if length == float("inf") else length