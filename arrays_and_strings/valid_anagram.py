class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        tracker = {}

        for i in range(len(s)):
            tracker[s[i]] == tracker.get(s[i], 0) + 1

        for i in range(len(t)):
            if t[i] in tracker:
                tracker[t[i]] == tracker.get(t[i], 0) - 1
            else:
                return False
        
        for i in tracker:
            if tracker.get(i) != 0:
                return False
            else:
                return True
        
        #Complexity O(n)

        #Sorted comparison O(nlogn)
        #Bruteforce O(n^2)