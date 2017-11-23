class Solution:
    def repeatedSubstringPattern(self, s):
        return (s in ((s*2)[1:-1]))

# creates a string formed by appending s to s
# then removes the first and last character
# if s appears in this string, then it must be true