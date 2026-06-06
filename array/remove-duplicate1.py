from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        # the first element will be always unique so we can skip first element
        # with 00112
        c = 1
        for i in range(1, len(nums)):
            # c = number of unique element so far
            # c-1 = last unique element index
            # i = 1, c = 1 => skip
            # i = 2, c = 1 => nums[2] = 1, nums[c-1] = 0 (new element found), nums = 01112
            # i = 3, c = 2 =>
            if nums[i] != nums[c - 1]:
                nums[c] = nums[i]
                c += 1

        return c


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 2]))  # Output: 3
