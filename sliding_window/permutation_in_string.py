class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1: return True
        s1_map, s2_map = {}, {}
        match, l = 0, 0
        if len(s1) > len(s2): return False
        
        for c in range(len(s1)):
            s1_map[s1[c]] = 1 + s1_map.get(s1[c], 0)
            s2_map[s2[c]] = 1 + s2_map.get(s2[c], 0)
        print(s1_map, s2_map)
        
        for c in s1_map:
            if s1_map[c] == s2_map.get(c, 0):
                match += 1
        
        if match == len(s1_map): return True
                
        for r in range(len(s1), len(s2)):
            if match == len(s1_map): return True
            match = 0
            
            #shift/ modify left
            s2_map[s2[l]] -= 1
            l += 1
            
            #modify right
            s2_map[s2[r]] = 1 + s2_map.get(s2[r], 0)
            
            #compare maps
            for c in s1_map:
                if s1_map[c] == s2_map.get(c, 0):
                    match += 1
        return match == len(s1)
            
        #Complexity O(26.n)
        #Space O(n)