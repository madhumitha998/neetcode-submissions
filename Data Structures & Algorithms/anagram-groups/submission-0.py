class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we will have a running hm of unique ordered strs to the actual str
        #if not in the hm, add as new entry if not add to existing ordered key
        ordered_str_hm = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in ordered_str_hm:
                ordered_str_hm[sorted_str] = [string]
            else:
                ordered_str_hm[sorted_str].append(string)
        
        return list(ordered_str_hm.values());