class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        dict = {}
        while len(s) != 0:
            x = next(iter(s))
            while s.__contains__(x-1):
                x = x-1
            #cur_item = x
            #if not s.__contains__(x-1):
            dict[x] = 1
            s.remove(x)
            cur_item = x+1
            while s.__contains__(cur_item):
                dict[x] +=1
                s.remove(cur_item)
                cur_item +=1
        if len(dict) == 0:
            return 0
        else:
            return max(dict.values())

        