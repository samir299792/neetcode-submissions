class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        len_s = len(sorted_s)
        len_t = len(sorted_t)

        if sorted_s == sorted_t and len_s == len_t:
            return True
        else:
            return False