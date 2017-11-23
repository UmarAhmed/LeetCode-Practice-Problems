class Solution:
    def thirdMax(self, nums):
        if len(set(nums)) < 3:
            return max(nums)
        else:
            return sorted(set(nums))[-3]

# This solution works... but  a better solution would be to keep an accumulator as you iterate through
# nums, and then to return the appropriate value
