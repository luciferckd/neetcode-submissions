class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        has_map = {}

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s not in has_map:
                has_map[sorted_s] = []
            has_map[sorted_s].append(s)
        return list(has_map.values())