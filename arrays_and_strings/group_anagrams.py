class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        
        for each_str in strs:
            count = [0] * 26
            for charac in each_str:
                count[ord(charac) - ord('a')] += 1
            
            hashmap[tuple(count)].append(each_str)
            
        return hashmap.values()
                
        #Complexity hashmap O(m * n)
        #Sort O(m * nlogn)
        #Brute force O(m * n * n)