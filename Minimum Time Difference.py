class Solution:
    def findMinDifference(self, timePoints):
        x = sorted([60*int((i.split(':'))[0]) + int((i.split(':'))[1]) for i in timePoints])
        return min(min([(x[i+1] - x[i]) for i in range(len(x) - 1)]),  (x[0] - x[-1])%1440)

# 1440 = 24*60, modulo accounts for circular difference

