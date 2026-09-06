class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        set_length = len(set(nums))
        if length == set_length:
            return False
        else:
            return True