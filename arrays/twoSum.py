class twoSum:
    def solution(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.

        Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]
        """
        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index
        return []

def main():
    solver = twoSum()

    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solver.solution(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}, Output: {result1}")  # Expected: [0, 1]

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solver.solution(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}, Output: {result2}")  # Expected: [1, 2]

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solver.solution(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}, Output: {result3}")  # Expected: [0, 1]

if __name__ == "__main__":
    main()