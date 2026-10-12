class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            if a>0:
                break
            left = i+1
            right = len(nums)-1
            while left < right:
                curSum = a + nums[left] + nums[right]
                if (curSum==0):
                    res.append([a, nums[left], nums[right]])
                    left +=1
                    while left < right and nums[left]==nums[left-1]:
                        left +=1
                elif curSum < 0:
                    left +=1
                else:
                    right -=1
        return res