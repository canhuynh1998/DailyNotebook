# Question Name: Concatenation of Array
- [link](https://leetcode.com/problems/concatenation-of-array/submissions/)

# Pattern
- Ad-hoc

# Explaination
- Duplicate the input array

# Pseudocode
concatinated = [0] * n
for idx, num in enumerate(nums):
    concatinated[idx] = num
    concatinated[idx + n] = num


# Solution
```python
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concatenated = [0] * (2 * n)

        for idx, num in enumerate(nums):
            concatenated[idx] = num
            concatenated[idx + n] = num
        return concatenated
```
