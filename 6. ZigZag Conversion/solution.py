#encoding=utf-8

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row_seq = []
        for i in range(numRows):
            row_seq.append([])

        i = 0
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    row_seq[j].append(s[i])
                    i += 1

            for j in range(numRows-2, 0, -1):
                if i < len(s):
                    row_seq[j].append(s[i])
                    i += 1

        ret = ''
        for seq in row_seq:
            ret += ''.join(seq)

        return ret

so = Solution()
print so.convert('ABC', 2)