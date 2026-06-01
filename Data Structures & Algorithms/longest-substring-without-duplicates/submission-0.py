class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        total_length = 0
        hashmap = {}

        for right in range(len(s)):
            if s[right] in hashmap and hashmap[s[right]] >= left:
                left = hashmap[s[right]] + 1
            
            hashmap[s[right]] = right
            total_length = max(total_length, right - left + 1)

        return total_length
        