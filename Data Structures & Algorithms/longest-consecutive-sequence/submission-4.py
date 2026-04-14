class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if len(nums) < 1:
        #     return 0

        # length = 1
        # longest = 1

        # nums.sort()

        # for i in range(len(nums) - 1):

        #     if nums[i] + 1 == nums[i + 1]:
        #         length += 1
        #         longest = max(length, longest)
        #     elif nums[i] == nums[i + 1]:
        #         continue
        #     else:
        #         length = 1

        # return longest


        length = 0
        longest = 0

        s = set(nums)

        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1

                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)

        return longest
        