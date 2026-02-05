# Question Name: Two Sum

# Pattern 
- Hash Map

# Explaination - Question
- What happens if there is not solution?
- Are the input valid?
- Since we are returing the indicies, do they have to be in order?

## Explaination
- If we have not encountered potential(potential = target - num)
  - Then we `must` store num since num is coming from the input array
  
# Pseudocode
- used hash map
-   target = a + b
    b = target - a
- Every iteration, leverage the above math formula, we can check if we have seen b via the hash map
    - if yes, we have the solution
    - else, put b in the hash map as key and value is the index

# Solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
    look_up = {}

    for idx, num in enumerate(nums):
        potential = target - num
        if potential not in look_up:
            look_up[num] = idx
        else:
            return [ idx, look_up[potential]]
    return [0,0]

