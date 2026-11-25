class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n

        for i in range(n - 1):
            mx = 0
            for j in range(i + 1, n):
                mx = max(mx, arr[j])
            res[i] = mx

        return res
        