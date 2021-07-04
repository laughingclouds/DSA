class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return list(map(int, str(int(''.join([str(x) for x in digits])) + 1)))
