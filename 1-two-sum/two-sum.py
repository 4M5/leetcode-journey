class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[diff],i]

