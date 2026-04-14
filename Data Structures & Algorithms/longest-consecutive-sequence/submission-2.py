class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0

        length = 1
        longest = 1

        nums.sort()

        for i in range(len(nums) - 1):

            if nums[i] + 1 == nums[i + 1]:
                length += 1
                longest = max(length, longest)
            elif nums[i] == nums[i + 1]:
                continue
            else:
                length = 1

        return longest
        