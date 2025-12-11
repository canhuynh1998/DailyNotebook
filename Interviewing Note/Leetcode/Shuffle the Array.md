# Question Name: Shuffle the Array
- [link](https://leetcode.com/problems/shuffle-the-array/description)

# Pattern
- Two pointers

# Explaination
- The input array is even length
- Split the input into 2 parts. Treat them as 2 different arrays
  - Alternatively put the number in the output array

# Pseudocode
1 pass
shuffled = [0] * 2 * n
i = 0
for idx in range(n):
    shuffled[i] = input[idx]
    i += 1
    shuffled[i] = input[idx + n]
    i += 1
# Solution

```python
  def shuffle(self, nums: List[int], n: int) -> List[int]:
      shuffled = [0] * len(nums)
      idx = 0
      i = 0
      for idx in range(n):
          shuffled[i] = nums[idx]
          i += 1
          shuffled[i] = nums[idx + n]
          i += 1

      return shuffled
```

