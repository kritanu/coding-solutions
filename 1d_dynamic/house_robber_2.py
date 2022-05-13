class Solution:
    def rob(self, nums: List[int]) -> int:
        return (max(nums[0], self.plain_rob(nums[1:]), self.plain_rob(nums[:-1])))
        
    # [ rob1, rob2, n, n+1,.... ]
    def plain_rob(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            rob_max = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = rob_max
        return rob_max
            
        
        #Complexity O(2n) = O(n), space O(1)
        #brute O(n^2)
        