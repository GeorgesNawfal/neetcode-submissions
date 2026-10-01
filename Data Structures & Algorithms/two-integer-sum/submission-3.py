class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in lst:
                return [lst[remain], i]
            lst[nums[i]] = i
