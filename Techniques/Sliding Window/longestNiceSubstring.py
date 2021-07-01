import re

class solution:
    def longestNiceSubstring(self, s: str) -> str:
        l = len(s)
        if l > 2:
            not_unique = set(s) - set(s.swapcase())

            if not not_unique:
                return s
            
            parts = re.split(f"[{''.join(not_unique)}]", s)
            return max(map(self.longestNiceSubstring, parts), key=len)
        
        if l == 2:
            if s[0] == s[1].swapcase():
                return s
        return ""