# Algorithm Problems Collection

This repository contains implementations of several classic algorithmic problems, demonstrating various dynamic programming techniques and recursive approaches. Each solution is implemented in Python with a focus on efficiency and readability.

## Table of Contents

- [Longest Increasing Subsequence](#longest-increasing-subsequence)
- [Maximum Sum Subarray](#maximum-sum-subarray)
- [Non-Decreasing Component Sequences](#non-decreasing-component-sequences)
- [Lexicographic Permutations](#lexicographic-permutations)
- [Optimal Game Strategy](#optimal-game-strategy)

## Longest Increasing Subsequence

### Problem Description
Find the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.

### Example
**Input:** `[10, 22, 9, 33, 21, 50, 41, 60, 80]`  
**Output:** `[10, 22, 33, 50, 60, 80]`

### Algorithm Approach
This solution uses a **Dynamic Programming** approach with O(n²) time complexity:
- Tracks the length of LIS ending at each index
- Maintains previous indices to reconstruct the sequence

### Visualization

```
Input array: [10, 22, 9, 33, 21, 50, 41, 60, 80]

Step-by-step solution:
1. Initialize arrays:
   - subsequence_lengths = [1, 1, 1, 1, 1, 1, 1, 1, 1]
   - previous_indices = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

2. For each element, check if it can extend any existing subsequence:
   
   Pass 1: For 22 (index 1)
   22 > 10, so update:
   - subsequence_lengths = [1, 2, 1, 1, 1, 1, 1, 1, 1]
   - previous_indices = [-1, 0, -1, -1, -1, -1, -1, -1, -1]

   Pass 3: For 33 (index 3)
   33 > 22, and subsequence_lengths[1] + 1 > 2, so update:
   - subsequence_lengths = [1, 2, 1, 3, 1, 1, 1, 1, 1]
   - previous_indices = [-1, 0, -1, 1, -1, -1, -1, -1, -1]

   ... and so on

3. Final state:
   - subsequence_lengths = [1, 2, 1, 3, 2, 4, 4, 5, 6]
   - previous_indices = [-1, 0, -1, 1, 0, 3, 3, 5, 7]
   
4. Backtrack to construct the solution: [10, 22, 33, 50, 60, 80]
```

## Maximum Sum Subarray

### Problem Description
Find a contiguous subarray with the largest sum within a given array of integers.

### Example
**Input:** `[2, -4, 6, 8, -10, 100, -6, 5]`  
**Output:** `[6, 8, -10, 100]` with sum 104

### Algorithm Approach
This solution uses **Kadane's Algorithm** with O(n) time complexity:
- Tracks current sum and resets when it becomes negative
- Maintains indices to reconstruct the subarray

### Visualization

```
Input array: [2, -4, 6, 8, -10, 100, -6, 5]

Iteration:  0   1    2   3    4     5    6   7
           [2, -4,   6,  8,  -10,  100, -6,  5]
current:    2  -2    6  14    4    104  98  103
max:        2   2    6  14   14    104  104  104
start:      0   2    2   2    2     2    2    2
end:        0   0    2   3    3     5    5    5

Result: Maximum sum is 104, subarray is [6, 8, -10, 100]
```

## Non-Decreasing Component Sequences

### Problem Description
Generate all possible sequences of natural numbers that:
1. Sum up to a given target number n
2. Are non-decreasing (each element is greater than or equal to the previous one)

### Example
**Input:** `n = 5`  
**Output:**
```
1 1 1 1 1
1 1 1 2
1 1 3
1 2 2
1 4
2 3
5
```

### Algorithm Approach
This solution uses **Backtracking** with a recursive approach:
- Maintains a current sequence and minimum allowed value
- Only explores valid paths that maintain non-decreasing property

### Visualization

For n = 5, recursion tree:

```
                              Start(5, min=1)
                              /      |     \
                  [1](4,1)         [2](3,2)    [3](2,3)  [4](1,4)  [5](0,5)
                 /   |   \           /   \        |         |         |
       [1,1](3,1) [1,2](2,2) [1,3](1,3)  [2,2](1,2) [2,3](0,3) [3,4](0,4) [4,5](0,5)
```

Each node shows:
- Current sequence in brackets
- (Remaining sum, Minimum next value)
- Leaf nodes with remaining sum = 0 are valid solutions

## Lexicographic Permutations

### Problem Description
Generate all permutations of the first n letters of the alphabet in lexicographic order.

### Example
**Input:** `n = 3`  
**Output:**
```
abc
acb
bac
bca
cab
cba
```

### Algorithm Approach
This solution uses **Recursive Backtracking** to generate all permutations:
- Two implementations provided:
  1. `AlphabetPermutationGenerator`: Stores all permutations in memory
  2. `MemoryEfficientPermutationGenerator`: Prints permutations as they're generated
- Time complexity is O(n!) as expected

### Visualization

For n = 3, recursive tree:

```
                            Start
                     /       |       \
                   a(bc)    b(ac)    c(ab)
                  /   \     /   \    /   \
              ab(c)  ac(b) ba(c) bc(a) ca(b) cb(a)
                |     |     |     |     |     |
              abc    acb   bac   bca   cab   cba
```

## Optimal Game Strategy

### Problem Description
Two players take turns selecting either the first or last element from an array of integers. Each player aims to maximize their total score. Determine the maximum possible scores for both players if they play optimally.

### Example
**Input:** `[10, 15, 2, 7]`  
**Output:** `(22, 12)` where Player 1 gets 22 and Player 2 gets 12

### Algorithm Approach
This solution uses **Dynamic Programming** with memoization:
- Recursively calculates the maximum score difference achievable from any state
- Time complexity: O(n²) where n is the array length

### Visualization

For array `[10, 15, 2, 7]`:

The dynamic programming approach uses a matrix where `dp[i][j]` represents the maximum score difference (player1 - player2) when considering the subarray from index i to j.

For array `[10, 15, 2, 7]`:

**Step 1: Initialize diagonal (single element subarrays)**
Each player can only take the single element, so difference = that element value

```
    |  0  |  1  |  2  |  3  
----+-----+-----+-----+-----
 0  |  10 |     |     |     
----+-----+-----+-----+-----
 1  |     |  15 |     |     
----+-----+-----+-----+-----
 2  |     |     |  2  |     
----+-----+-----+-----+-----
 3  |     |     |     |  7  
```

**Step 2: Fill diagonal + 1 (subarrays of length 2)**
For each pair, player will choose the maximum element, leaving minimum for opponent:

```
    |  0  |  1  |  2  |  3  
----+-----+-----+-----+-----
 0  |  10 |  5 |     |     
----+-----+-----+-----+-----
 1  |     |  15 |  13 |     
----+-----+-----+-----+-----
 2  |     |     |  2  |  5 
----+-----+-----+-----+-----
 3  |     |     |     |  7  
```

For example, dp[0][1] = max(10-15, 15-10) = max(-5, 5) = 5, but as player 1 starts, they pick 15, making the difference -5

**Step 3: Fill diagonal + 2 (subarrays of length 3)**

```
    |  0  |  1  |  2  |  3  
----+-----+-----+-----+-----
 0  |  10 |  5 |  8  |     
----+-----+-----+-----+-----
 1  |     |  15 |  13 |  8  
----+-----+-----+-----+-----
 2  |     |     |  2  |  5 
----+-----+-----+-----+-----
 3  |     |     |     |  7  
```

For dp[0][2], player 1 can choose:
- Take 10, leaving [15,2] for player 2: 10 - dp[1][2] = 10 - 13 = -3
- Take 2, leaving [10,15] for player 2: 2 - dp[0][1] = 2 - (-5) = 7
Result: max(-3, 7) = 7

**Step 4: Fill diagonal + 3 (full array)**

```
    |  0  |  1  |  2  |  3  
----+-----+-----+-----+-----
 0  |  10 |  5 |  8  |  10 
----+-----+-----+-----+-----
 1  |     |  15 |  13 |  8  
----+-----+-----+-----+-----
 2  |     |     |  2  |  5 
----+-----+-----+-----+-----
 3  |     |     |     |  7  
```

For dp[0][3], player 1 can choose:
- Take 10, leaving [15,2,7] for player 2: 10 - dp[1][3] = 10 - 8 = 2
- Take 7, leaving [10,15,2] for player 2: 7 - dp[0][2] = 7 - 8 = -1
Result: max(2, -1) = 2

The final result dp[0][3] = 10 means player 1 will score 10 more points than player 2.


explain to me WHY this works



Where dp[i][j] = max score difference (player1 - player2) for subarray from index i to j.

The optimal play sequence:
1. Player 1 takes 7 (right end)
2. Player 2 takes 10 (left end)
3. Player 1 takes 15 (left end)
4. Player 2 takes 2 (remaining element)

Final scores: Player 1 = 22 (7 + 15), Player 2 = 12 (10 + 2)

## Running the Code

Each solution can be run independently:

```bash
python Zadanie_1.py  # Longest Increasing Subsequence
python Zadanie_2.py  # Maximum Sum Subarray
python Zadanie_3.py  # Non-Decreasing Component Sequences
python Zadanie_4.py  # Lexicographic Permutations
python main.py       # Optimal Game Strategy
```

## Testing

The Optimal Game Strategy solution includes unit tests:

```bash
pytest main_test.py -v
```