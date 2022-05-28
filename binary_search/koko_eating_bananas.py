class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) 
        res = r
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            
            for p in piles:
                hours += math.ceil(p / k)
                
            if hours <= h:
                res =  min(res, k)
                r = k - 1
            elif hours > h:
                l = k + 1
                
        return res
    
    #Complexity O(log(max(p)*p)), space O(1)
    #Brute O(max(p)*p)