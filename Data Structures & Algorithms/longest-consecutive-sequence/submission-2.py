class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for x in nums:
            if x - 1 not in num_set:

                cnt = 1
                cur = x

                while cur + 1 in num_set:
                    cur += 1
                    cnt += 1
            
                longest = max(longest, cnt)
        
        return longest

        