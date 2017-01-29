class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_out = 0
        tmp1 = l1
        tmp2 = l2
        tv1 = l1.val
        tv2 = l2.val
        love = ListNode(0)
        tmp = love
        while 1 :
            tv = tv1+tv2
            if carry_out == 1 :
                tv+=1
                carry_out = 0
            if tv > 9 :
                tv -= 10
                carry_out = 1
            tmp.val = tv
            if (tmp1.next == None) and (tmp2.next  == None) :
                if carry_out == 1:
                    haha = ListNode(1)
                    tmp.next = haha
                return love;
            if (tmp1.next == None) :
                tv1 = 0
            else:
                tmp1 = tmp1.next
                tv1 = tmp1.val
            if (tmp2.next == None) :
                tv2 = 0
            else:
                tmp2 = tmp2.next
                tv2 = tmp2.val
            haha = ListNode(0)
            tmp.next = haha
            tmp = tmp.next