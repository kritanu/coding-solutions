class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
            
        for n, c in hashmap.items():
            freq[c].append(n)
           
        res = []
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        #Complexity O(n) - bucket sort
        #hashmap + sort - O(nlogn))
        #brute force O(n^2)