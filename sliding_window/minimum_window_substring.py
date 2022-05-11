class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""
        
        have_map, need_map = {}, {}
        
        #create characters needed (t)
        for c in t:
            need_map[c] = 1 + need_map.get(c, 0)
        
        have, need = 0, len(need_map)
        res, res_length = [-1, -1], float("infinity")
        
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            have_map[c] = 1 + have_map.get(c, 0)
            
            if c in need_map and have_map[c] == need_map[c]:
                have += 1
                
            while have == need:
                if r - l + 1 < res_length:
                    res = [l, r]
                    res_length = r - l + 1
                
                #pop c from left
                have_map[s[l]] -= 1
                if s[l] in need_map and have_map[s[l]] < need_map[s[l]]:
                    have -= 1
                l += 1
                
        return s[res[0]:res[1]+1] if res_length != float("infinity") else ""
        
        #Complexity O(n)
        #Brute force O(n^3)