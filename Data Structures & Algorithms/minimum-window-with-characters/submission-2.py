from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        target = Counter(t)
        window = {}

        required = len(target)
        formed = 0

        L = 0
        min_win = float("inf")
        best_L, best_R = 0, 0

        for R in range(len(s)):
            c = s[R]
            window[c] = window.get(c, 0) + 1

            # A required character's frequency is satisfied
            if c in target and window[c] == target[c]:
                formed += 1

            # Shrink while the window is valid
            while formed == required:

                # Save the smallest valid window
                if R - L + 1 < min_win:
                    min_win = R - L + 1
                    best_L, best_R = L, R

                # Remove the leftmost character
                left_char = s[L]
                window[left_char] -= 1

                # Check whether removing it breaks validity
                if left_char in target and window[left_char] < target[left_char]:
                    formed -= 1

                L += 1

        if min_win == float("inf"):
            return ""

        return s[best_L:best_R + 1]