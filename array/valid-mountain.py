from typing import List

"""


"""


class Solution:
    def is_valid_mountain(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        if n < 3:
            return False

        # try to climb up
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # check if the peak is not 0 or n - 1
        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        return i == n - 1


if __name__ == "__main__":
    print(Solution().is_valid_mountain([0, 2, 3, 4, 5, 3, 0]))
    print(Solution().is_valid_mountain([0, 2, 3, 3, 5, 2, 1, 0]))
