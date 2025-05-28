from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        array = [0] * (len(nums1) + len(nums2))
        index1 = 0
        index2 = 0
        index = 0
        while index1 < len(nums1) or index2 < len(nums2):
            if index1 < len(nums1) and index2 < len(nums2):
                if nums1[index1] < nums2[index2]:
                    array[index] = nums1[index1]
                    index1 += 1
                    index += 1
                else:
                    array[index] = nums2[index2]
                    index2 += 1
                    index += 1
            else:
                if index1 < len(nums1):
                    array[index] = nums1[index1]
                    index1 += 1
                    index += 1
                if index2 < len(nums2):
                    array[index] = nums2[index2]
                    index2 += 1
                    index += 1


        midIndex = len(array) // 2
        return (array[midIndex] + array[midIndex - 1]) / 2 if len(array) % 2 == 0 else array[midIndex]

if __name__ == '__main__':
    list1 = [1, 3]
    list2 = [2, 4]
    res = Solution.findMedianSortedArrays(Solution, list1, list2)
    print(res)
