class Solution:
    def singleNonDuplicate(self, nums):
        for i in set(nums):
            if nums.count(i) == 1:
                return i

# could also do a binary search, but this runs fine
# O(m), where m is the number of distinct elements in nums