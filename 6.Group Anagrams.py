'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

from collections import  defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        d= defaultdict(list)
        for i in strs:
    
            k=''.join(sorted(i))
        
            d[k].append(i)
        return d.values()