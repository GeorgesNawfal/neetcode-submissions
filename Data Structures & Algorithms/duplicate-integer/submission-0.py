class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = {}
        for i in nums:
            if not i in lst:
                lst[i] = i
            else:
                return True
        return False