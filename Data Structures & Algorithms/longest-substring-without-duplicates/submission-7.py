class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len, L = 0, 0
        seen = set()

        for R in range(len(s)):
            
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            cur_len = R - L + 1
            max_len = max(max_len, cur_len)
            seen.add(s[R])
        return max_len