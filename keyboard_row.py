class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1 = set([*"qwertyuiop"])
        row2 = set([*"asdfghjkl"])
        row3 = set([*"zxcvbnm"])
        rows = [row1, row2, row3]
        
        res = []
        
        for word in words:
            for row in rows:
                if set([*word.lower()]).issubset(row):
                    res.append(word)
                    break
                    
        return res