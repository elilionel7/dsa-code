class Solution:

  def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    maxArea = 0
    n = len(heights)

    for i in range(n + 1):
      h = 0 if i == n else heights[i]
      while stack and heights[stack[-1]] > h:
        index = stack.pop()
        height = heights[index]
        width = i - stack[-1] - 1 if stack else i
        maxArea = max(maxArea, height * width)
      stack.append(i)

    return maxArea
