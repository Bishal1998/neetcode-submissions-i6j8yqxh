class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        required = len(need)
        window = {}
        matches = 0
        result = float("inf"), 0, 0
        left = 0

        for right in range(len(s)):

            c = s[right]
            window[c] = window.get(c, 0) +1

            if c in need and need[c] == window[c]:
                matches += 1

            while matches == required:
                if (right - left + 1) < result[0]:
                    result = (right - left + 1, left, right)
                
                left_char = s[left]
                if left_char in need and need[left_char] == window[left_char]:
                    matches -= 1
                
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]

                left += 1
        return s[result[1] : result[2] + 1] if result[0] != float("inf") else ""
        