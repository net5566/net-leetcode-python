class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = 0
        flag = 0
        if x is 0:
            return 0
        if x < 0:
            flag = 1
            x *= -1
        else :
            flag = 0
        while x != 0:
            out = out*10 + x % 10
            x= int(x/10)
        if flag is 1:
            out *= -1
        if out < -2147483647 or out > 2147483646 :
            return 0
        return out