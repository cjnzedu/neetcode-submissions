class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1 = {}
        h2 = {}

        for v in s:
            if v in h1:
                h1[v] += 1
            else:
                h1[v] = 1
        for v in t:
            if v in h2:
                h2[v] += 1
            else:
                h2[v] = 1
        
        return h1 == h2
