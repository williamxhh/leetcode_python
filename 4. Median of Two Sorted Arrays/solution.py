#encoding=utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i, j, count = 0, 0, 0
        m = len(nums1)
        n = len(nums2)
        while (count < (m+n)/2) and (i < m) and (j < n):
            if nums1[i] <= nums2[j]:
                val = nums1[i]
                i += 1
                count += 1
            else:
                val = nums2[j]
                j += 1
                count += 1

        while count < (m+n)/2:
            if i < m:
                i += (m+n)/2 - count
                count = (m+n)/2
                val = nums1[i-1]
            elif j < n:
                j += (m+n)/2 - count
                count = (m+n)/2
                val = nums2[j-1]

        if (i < m) and (j < n):
            nextval = min(nums1[i], nums2[j])
        elif i < m:
            nextval = nums1[i]
        else:
            nextval = nums2[j]

        if (m+n)%2 == 1:
            return nextval
        else:
            return float(val+nextval)/2

so = Solution()
print so.findMedianSortedArrays([],[2,3])