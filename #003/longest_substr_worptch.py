class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myHash = {}
        
        max=0
        head=0
        tail=-1
        slen=len(s)
        tmp=0

        for i in range(slen):
            tail += 1
            key = ord(s[i]) % 97
            if key in myHash:
                while head <= tail:
                    if(slen - head -1 < max):
                        return max
                        
                    if s[head] == s[i]:
                        head += 1
                        break
                    else:
                        key = ord(s[head]) % 97
                        del myHash[key]
                        head += 1
                        tmp -= 1
            else:
                myHash[key] = s[i]
                tmp += 1

            if tmp > max:
                max = tmp
                
        return max