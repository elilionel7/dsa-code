class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for c in s:
            if not c.isalnum():
                continue

            cleaned += c.lower()

        return cleaned == cleaned[::-1]
        