class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        left = 1
        while x / left >= 10:
            left *= 10
        right = 10
        
        while left >= right:
            if int(x/left) != x%right :
                return False
            else:
                x = x% left
                x = int(x/10)
                left /= 10
                
        return True