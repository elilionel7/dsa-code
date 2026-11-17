class Solution:

  def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    maxArea = 0

    # Append 0 to force all remaining bars in the stack to be popped at the end
    for i, h in enumerate(heights + [0]):
      while stack and heights[stack[-1]] > h:
        index = stack.pop()
        height = heights[index]
        width = i - stack[-1] - 1 if stack else i
        maxArea = max(maxArea, height * width)
      stack.append(i)

    return maxArea
