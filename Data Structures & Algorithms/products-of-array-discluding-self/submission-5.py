class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
       
        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]
        
        pro = 1
        for i in range(n-1,-1,-1):
            pref[i] *= pro
            pro *= nums[i]
        
        return pref
            

