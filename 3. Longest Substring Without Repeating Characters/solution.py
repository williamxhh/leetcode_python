#encoding=utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        characters = []
        for i in range(len(s)):
            while s[i] in characters:
                characters.pop(0)
            characters.append(s[i])
            max_len = max(max_len, len(characters))

        return max_len

