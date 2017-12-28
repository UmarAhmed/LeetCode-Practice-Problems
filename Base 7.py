class Solution:
    def convertToBase7(self, num):
        f = ""
        if num < 0:
            f = "-"
        return f + self.conv(abs(num), 7)

    def conv(self, n, b):
        c = "0123456789abcdefghijklmnopqrstuvwxyz"
        if n < b:
            return c[n]
        else:
            return self.conv(n // b, b) + c[n % b]