
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters_seen = {}
        letters_wanted = {}

        if len(t) > len(s):
            return ""

        for char in t:
            letters_wanted[char] = letters_wanted.get(char, 0) + 1

        left = 0
        min_length = float("inf")
        result = ""

        have = 0
        need = len(letters_wanted)

        for right in range(len(s)):
            char_right = s[right]
            letters_seen[char_right] = letters_seen.get(char_right, 0) + 1

            # A character's requirement has been satisfied
            if char_right in letters_wanted:
                if letters_seen[char_right] == letters_wanted[char_right]:
                    have += 1

            while have == need:
                if right - left + 1 < min_length:
                    result = s[left:right + 1]
                    min_length = right - left + 1

                char_left = s[left]
                letters_seen[char_left] -= 1

                # A character's requirement is no longer satisfied
                if char_left in letters_wanted:
                    if letters_seen[char_left] < letters_wanted[char_left]:
                        have -= 1

                left += 1

        return result
