class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # hashmap_s = {}
        # hashmap_t = {}

        # if len(s) != len(t):
        #     return False

        # for i in range(len(s)):

        #     hashmap_s[s[i]] = hashmap_s.get(s[i], 0) + 1
        #     hashmap_t[t[i]] = hashmap_t.get(t[i], 0) + 1

        # return hashmap_s == hashmap_t

        if len(s) != len(t):
            return False

        count = {}

        for a, b in zip(s,t):
            count[a] = count.get(a, 0) + 1
            count[b] = count.get(b, 0) - 1

        for v in count.values():
            if v != 0:
                return False
        return True
        