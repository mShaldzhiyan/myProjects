def findMedianSortedArrays(nums1, nums2) -> float:
    array = nums1 + nums2
    ret = sorted(array)
    if ((len(ret) % 2) != 0):
        return ret[len(ret / 2 + 1)]
    else:
        return (ret[len(ret / 2 + 1)] + ret[len(ret / 2)]) / 2

print(findMedianSortedArrays([1,3], [2]))