class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        l, k, maxL = 0, 0, 1
        prev_dir, cur_dir = None, None
        
        for r in range(1, len(nums)):
            if nums[r] > nums[k]:
                cur_dir = "up"
            if nums[r] < nums[k]:
                cur_dir = "down"
            if nums[r] == nums[k]:
                cur_dir = None

            if cur_dir != prev_dir and cur_dir != None:
                maxL = max(maxL, r-l+1)
            elif cur_dir == None:
                l = r
            else:
                l = k
            prev_dir = cur_dir
            k = r
 
        return maxL