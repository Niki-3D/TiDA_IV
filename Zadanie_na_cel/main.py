from functools import lru_cache
from typing import List, Tuple

def max_scores(nums: List[int]) -> Tuple[int, int]:
    n = len(nums)

    @lru_cache(None)
    def dp(i: int, j: int) -> int:
        if i == j:
            return nums[i]
        return max(nums[i] - dp(i + 1, j), nums[j] - dp(i, j - 1))

    total = sum(nums)
    diff = dp(0, n - 1)

    player1 = (total + diff) // 2
    player2 = total - player1
    return (player1, player2)
