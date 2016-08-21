#encoding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_mapping = {}
        for i in range(len(nums)):
            if (target - nums[i]) in index_mapping and index_mapping[target - nums[i]] != i:
                return sorted([i, index_mapping[target - nums[i]]])
            index_mapping[nums[i]] = i

        return [-1, -1]