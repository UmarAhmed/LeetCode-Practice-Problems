class Solution:
    def findWords(self, words):
        k = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        return [i for i in words if set(i.lower()) - set(k[0]) == set() or set(i.lower()) - set(k[1]) == set()
                or set(i.lower()) - set(k[2]) == set()]
