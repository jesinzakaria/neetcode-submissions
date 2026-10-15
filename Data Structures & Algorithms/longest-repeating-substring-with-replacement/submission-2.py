class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r-l+1) - max(count.values()) <= k:
                result = max(result, r-l+1)
            else:
                while (r-l+1) - max(count.values()) > k:
                    count[s[l]] -= 1  
                    l += 1
        return result

        