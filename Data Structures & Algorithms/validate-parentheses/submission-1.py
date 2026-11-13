class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for p in s:
            if p in pairs:
                if stack and stack[-1] == pairs[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return not stack


        