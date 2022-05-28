class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp_array = [0] * (n+1)
        offset = 1
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp_array[i] = 1 + dp_array[i - offset]
            
        return dp_array
    
    #brute force O(nlogn) - %, // operations
    #Complexity O(n)