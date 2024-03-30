class Solution(object):
    def runningSum(self, nums):
        # 1.Store the list e.g.: [1,2,3]
        output_arr = []
        # 2. Repeat the process until the last position len(list) 
        for i in range(0, len(nums) -1 ):
        # 3. If is the first position read the first element [i] and store the number in other list
            if i == 0:
                output_arr.append(nums[i])
                output_arr.append(nums[i] + nums[i+1])
        # 4. If is other position than the first one, sum the current element [i] and sum with the last element [i-1]
            else:
                output_arr.append(output_arr[i] + nums[i+1])        
        # 5. -1 and return the output array
        return output_arr
# Define the Running sun array
input_arr = [3,1,2,10,1]
# Object to store the solution
solution = Solution()
# Call the function passing the list
result = solution.runningSum(input_arr)
# Print the return
print(result)



"""
:type nums: List[int]
:rtype: List[int]
"""
