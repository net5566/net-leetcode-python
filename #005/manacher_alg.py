class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        span = []

        for i in range(len(s)):
            span.append('\t')
            span.append(s[i])
        span.append('\t')

        head = 0
        tail = 0
        max = 0

        for i in range(len(span)):
            if(max/2+i>len(span)):
                break
            tmp = 0
            x=i
            y=i
            while(x>=0 and y<sl):
                if(span[x] is span[y]):
                    tmp+=2
                    x -= 1
                    y += 1
                else:
                    break
            if(tmp >= max):

                head = (x+1)/2
                tail = (y-1)/2
                max = tmp

        return s[head:tail]