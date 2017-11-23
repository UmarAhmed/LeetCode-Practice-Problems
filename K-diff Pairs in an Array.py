class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        if k == 0:
            return sum(i > 1 for i in collections.Counter(nums).values())
        else:
            return len(set(nums) & set([i + k for i in nums]))
