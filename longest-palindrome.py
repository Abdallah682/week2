class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for char in s:
            if char in letters: letters[char]+=1
            else: letters[char]=1
        palindrome = 0 #base case, longest palindrome is one
        extra = 0
        for letter in letters:
            if letters[letter]>1:
                increment = letters[letter]//2
                letters[letter]-=(increment*2)
                palindrome+=(increment*2)
            if extra==0 and letters[letter]==1:
                extra = 1
        return palindrome+extra