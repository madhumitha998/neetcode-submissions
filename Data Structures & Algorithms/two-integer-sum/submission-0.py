class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a map of each number to its complement of target
        index_to_num = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in index_to_num:
                index_to_num[num] = i
            else:
                return [index_to_num[complement], i]
