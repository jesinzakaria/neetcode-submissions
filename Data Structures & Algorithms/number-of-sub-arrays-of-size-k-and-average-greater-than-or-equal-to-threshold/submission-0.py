class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        l = 0
        curSum = 0
        target = k*threshold
        #print(target)
        arrayCount = 0
        for r in range(len(nums)):
            curSum += nums[r]
            if (r-l+1) == k:
                if (curSum >= target):
                    arrayCount += 1
                    #print(curSum)
                curSum -= nums[l]
                l+=1 
        return arrayCount       