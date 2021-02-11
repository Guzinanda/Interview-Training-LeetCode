'''
@   Median of Two Sorted Arrays| 04

@   Problem
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
    the median of the two sorted arrays.
    
    Follow up: The overall run time complexity should be O(log (m+n)).

@   Example
    Input:  nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

@   Template

'''
    
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    len1 = len(nums1)
    len2 = len(nums2)
    # when total length is odd, the median is the middle
    if (len1 + len2) % 2 != 0:
        return self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
    else:
    # when total length is even, the median is the average of the middle 2
        middle1 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
        middle2 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2-1)
        return (middle1 + middle2) / 2

def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
    if start1 > end1:
        return nums2[k-start1]
    if start2 > end2:
        return nums1[k-start2]
        
    middle1 = (start1 + end1) // 2
    middle2 = (start2 + end2) // 2
    middle1_value = nums1[middle1]
    middle2_value = nums2[middle2]
        
    # if sum of two median's indicies is smaller than k
    if (middle1 + middle2) < k:
        # if nums1 median value bigger than nums2, then nums2's first half will 
        # always be positioned before nums1's median, so k would never be in 
        # num2's first half
        if middle1_value > middle2_value:
            return self.get_kth(nums1, nums2, start1, end1, middle2+1, end2, k)
        else:
            return self.get_kth(nums1, nums2, middle1+1, end1, start2, end2, k)
    # if sum of two median's indicies is bigger than k
    else:
        # if nums1 median value bigger than nums2, then nums2's first half would 
        # be merged before nums1's first half, thus k always come before nums1's 
        # median, then nums1's second half would never include k
        if middle1_value > middle2_value:
            return self.get_kth(nums1, nums2, start1, middle1-1, start2, end2, k)
        else:
            return self.get_kth(nums1, nums2, start1, end1, start2, middle2-1, k)


# TEST _______________________________________________________________________________

nums1 = [1,3]
nums2 = [2]

print(findMedianSortedArrays(nums1, nums2))
