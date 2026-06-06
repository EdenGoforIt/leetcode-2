from typing import List


# find if the arr can meet the condition: arr[j] = arr[i] * 2
# when 0 <= i, j < arr.length
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for n in arr:
            # if the vlaue is dividable means we satisify arr[j]
            if n * 2 in s or (n % 2 == 0 and n // 2 in s):
                return True

            s.add(n)

        return False


if __name__ == "__main__":
    s = Solution()

    # print(s.checkIfExist([10, 2, 5, 3]))  # Output: trued
    # print(s.checkIfExist([7, 1, 14, 11]))  # Output: true
    print(s.checkIfExist([-16, -13, 8]))  # Output: false
