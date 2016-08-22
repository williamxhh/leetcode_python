#encoding=utf-8

def expandAround(s, left, right):
    while (left >= 0) and (right <= len(s) - 1) and (s[left] == s[right]):
        left -= 1
        right += 1

    return s[left+1:right]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 0
        longest_str = ''
        for i in range(len(s)):
            l1 = expandAround(s, i, i)
            if len(l1) > longest:
                longest = len(l1)
                longest_str = l1

        for i in range(len(s) - 1):
            l2 = expandAround(s, i, i+1)
            if len(l2) > longest:
                longest = len(l2)
                longest_str = l2

        return longest_str

