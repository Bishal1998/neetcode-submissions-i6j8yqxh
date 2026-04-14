class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        count = 0

        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap.get(num, 0) + 1
            else:
                hashmap[num] = count + 1

            print(num, hashmap[num])

            if hashmap[num] > 1:
                return True
        return False
        