class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [(temperatures[0], 0)]

        for i in range(1, n):

            while stack and stack[-1][0] < temperatures[i]:
                _, day = stack.pop()
                answer[day] = i - day
            if not stack or stack[-1][0] >= temperatures[i]:
                stack.append((temperatures[i], i))
             
        return answer
                

        