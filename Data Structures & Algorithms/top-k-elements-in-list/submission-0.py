from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #order the values by descending and select the 0 - k-1 index of values and return their keys
        occurences_map = Counter(nums);
        most_common = occurences_map.most_common(k)
        #returns tuples of key and value (k,v) in a list []
        return [num for num, count in most_common]
         