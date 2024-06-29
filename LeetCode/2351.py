class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []
        for el in s:
            if el in seen:
                return el
            else:
                seen.append(el)