class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            s = ''.join(sorted(word))
            d.setdefault(s, []).append(word)
        
        return list(d.values())