class Solution:
    def largestPalindrome(self, n):
        if n == 1:
            return 9

        for i in range(2, 9 * 10 ** (n - 1)):
            upperBound = (10 ** n) - i
            lowerBound = int(str(upperBound)[::-1])
            if i ** 2 - 4 * lowerBound >= 0 and (i ** 2 - 4 * lowerBound) ** 0.5 == int(
                            (i ** 2 - 4 * lowerBound) ** 0.5):
                return (lowerBound + 10 ** n * (10 ** n - i)) % 1337

# uses some math to find a better solution than a naive implementation