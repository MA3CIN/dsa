class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        reversed = 0
        temporary = x
        
        while temporary != 0:
            digit = temporary % 10
            reversed = reversed * 10 + digit
            temporary //= 10
        return x == reversed
