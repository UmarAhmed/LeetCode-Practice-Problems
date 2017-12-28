class Solution:
    def findComplement(self, num):
        return int(''.join([str(abs(int(i) - 1)) for i in "{0:b}".format(num)]), 2)
