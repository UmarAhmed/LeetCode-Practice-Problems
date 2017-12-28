class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        import math
        return math.ceil(math.log(buckets, (minutesToTest / minutesToDie + 1)))
    # we use log because we can use a binary system to number the "buckets"
    # and then see which combination of "pigs" die to discern the correct bottle.



