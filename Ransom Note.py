class Solution:
    def canConstruct(self, ransomNote, magazine):
        x = True
        if ransomNote == "":
            return True

        for i in set((list(ransomNote))):
            if ransomNote.count(i) <= magazine.count(i):
                pass
            else:
                x = False
                break
        return x
