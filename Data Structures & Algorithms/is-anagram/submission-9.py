class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # if len(s) != len(t):
        #     return False

        # count_s, count_t = {}, {}
        
        # for i in range(len(s)):
        #     count_s[s[i]] = count_s.get(s[i], 0) + 1
        #     count_t[t[i]] = count_t.get(t[i], 0) + 1

        # return count_s == count_t
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True 
