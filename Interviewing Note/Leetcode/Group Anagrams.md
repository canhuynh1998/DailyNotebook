# Question Name: Group Anagrams

# Pattern 
- Hash Map
- Utilize Tuple in Python

# Explaination
Problem
- input: str[[]]
- output: str[[]]
# Pseudocode
Pseudocode
- Utilize the definition of an anagram
    - Sort all the character and store the sorted string as a key
- Iterate over the input strings and put every string into this sorted method (O(n + mlogm))
    -> If existed in the map, we have another member

- Iterate over the input strings, count the occurances of character and a key is in form of a tuple(O(n + m))

for s in strs: -> O(N)
    key = build_key(s) -> O(mlogm) time; O(m) space
    if key not in look_up:
        look_up[key] = []
    else:
        look_up[key].append(s)
return look_up.values()

Time: O(N)
Space: O(N)


# Solution
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      look_up = {}
      for s in strs:
          key = self.build_key(s)
          if key in look_up:
              look_up[key].append(s)
          else:
              look_up[key] = [s]
      return list(look_up.values())
  
  def build_key(self, s):
      alphabet = [0] * 26
      for c in s:
          alphabet[ord(c) - 97] += 1
      return tuple(alphabet)
