class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {};
        hashmap_t = {};

        if len(s) != len(t):
            return False

        for a in s:
            hashmap_s[a] = hashmap_s.get(a, 0) + 1
        for b in t:
            hashmap_t[b] = hashmap_t.get(b, 0) + 1
        return hashmap_t == hashmap_s
          