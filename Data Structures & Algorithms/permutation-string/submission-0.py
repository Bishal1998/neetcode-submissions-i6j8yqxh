class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        need = {}
        window = {} 
        matches = 0
        k = len(s1)
        

        for c in s1:
            need[c] = need.get(c, 0) + 1

        required = len(need)
        
        for right in range(len(s2)):

            c = s2[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                matches += 1
            
            if right - left + 1 > k:
                left_char = s2[left]

                if left_char in need and window[left_char] == need[left_char]:
                    matches -= 1
            
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                left += 1

            if matches == required:
                return True

        return False
        