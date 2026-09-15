class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lead = {}
        
        for word in strs:
            key = ''.join(sorted(word))

            if key not in lead:
                lead[key] = []

            lead[key].append(word)
        return list(lead.values())
            
            