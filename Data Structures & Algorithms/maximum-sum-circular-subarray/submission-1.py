class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0

        current_max = 0
        best_max = nums[0]

        current_min = 0
        best_min = nums[0]

        for num in nums:
            total += num

            # Kadane's algorithm for maximum subarray
            current_max = max(num, current_max + num)
            best_max = max(best_max, current_max)

            # Kadane's algorithm for minimum subarray
            current_min = min(num, current_min + num)
            best_min = min(best_min, current_min)

        # If all values are negative, avoid considering an empty wrapping subarray.
        if best_max < 0:
            return best_max

        wrapping_sum = total - best_min

        return max(best_max, wrapping_sum)
        