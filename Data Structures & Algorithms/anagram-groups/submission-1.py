class Solution:
    def computeKey(self, s: str) -> tuple: 
        l = [0,]*26
        for c in s:
            l[ord(c)-ord('a')] +=1
        return tuple(l)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            t = self.computeKey(s)
            group.setdefault(t, []).append(s)
        return list(group.values())
