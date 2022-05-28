class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0
        for n in nums:
            rob_max = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = rob_max
        return rob_max
            
        
        #Complexity O(n), space O(1)
        #brute O(n^2)