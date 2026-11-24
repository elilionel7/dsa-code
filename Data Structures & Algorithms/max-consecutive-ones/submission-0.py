class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        max_1s = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                max_1s = max(max_1s, prev)
                prev = 0
            else:
                prev += 1
        return max(prev, max_1s)


        