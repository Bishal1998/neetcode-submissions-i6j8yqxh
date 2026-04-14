from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # dic = {}

        # for s in strs:
        #     w = "".join(sorted(s))
            
        #     if w in dic:
        #         dic[w].append(s)
        #     else:
        #         dic[w] = [s]

        # return list(dic.values())


        dic = defaultdict(list)

        for s in strs:

            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1 

            dic[tuple(count)].append(s)

        return list(dic.values())




        