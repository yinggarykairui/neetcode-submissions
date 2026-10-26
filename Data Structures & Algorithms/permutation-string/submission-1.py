class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts, s2_counts = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) - ord("a")] += 1
        if s1_counts == s2_counts:
            return True
        window_length = len(s1)
        left = 1
        right = window_length
        while left <= right and right < len(s2):
            s2_counts[ord(s2[left - 1]) - ord("a")] -= 1
            s2_counts[ord(s2[right]) - ord("a")] += 1
            if s1_counts == s2_counts:
                return True  
            left += 1
            right += 1
        return False

        