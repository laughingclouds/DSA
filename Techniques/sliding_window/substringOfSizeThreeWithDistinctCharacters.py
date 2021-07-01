class solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s) - 2):
            ss = s[i: i + 3]

            if ss[0] != ss[1] and ss[0] != ss[2] and ss[1] != ss[2]:
                count += 1
        return count