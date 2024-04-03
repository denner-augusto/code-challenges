class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        # 1. Create a object to store the output
        output_arr = []
        # 2. Read the current list element (nums[0][0]) and store in output_arr
        for row in range(len(nums)):
            for element in row:
                print(element, end =' ')
        # 3. Check if the length of the first list is equal to k --> checkLengthK()
        # 4. if is equal to k then go to the next list
        # 5. If is not, then Read the second element (nums[0][1]) and checkLengthK()
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return print()
        # return nums

input_arr, k = [[1, 2, 3, 4], [5, 6], [7, 8, 9]], 2

solution = Solution()

result = solution.subarraysWithKDistinct(input_arr, k)

print(result)