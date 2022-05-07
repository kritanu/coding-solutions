class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n:
            res += n % 2
            n = n >> 1
        return res
    
    #Complexity of 0(1) = len(int num)