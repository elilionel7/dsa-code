
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] > h:
                index = stack.pop()
                height = heights[index]

                width = i - stack[-1] - 1 if stack else i

                maxArea = max(maxArea, height * width)

            stack.append(i)

        # Process remaining bars
        while stack:
            index = stack.pop()
            height = heights[index]

            width = n - stack[-1] - 1 if stack else n

            maxArea = max(maxArea, height * width)

        return maxArea



        