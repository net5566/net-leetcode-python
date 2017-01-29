class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    	myHash = {}
    	for i in range(len(nums)):
        	if target-nums[i] in myHash:
        		return (myHash[target-nums[i]]+1,i+1)
        	myHash[nums[i]]=i