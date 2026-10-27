class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        s = set()
        for r in range(len(nums)):
            if s.__contains__(nums[r]):
                return True
            s.add(nums[r])
            if (r-l) == k:
                s.remove(nums[l])
                l+=1 
        return False
        