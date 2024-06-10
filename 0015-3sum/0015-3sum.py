class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates and use the two-pointer technique
        finl = []
        
        for fixed_int in range(len(nums)):
            if fixed_int > 0 and nums[fixed_int] == nums[fixed_int - 1]:
                continue  # Skip duplicates for the fixed number
            
            st = fixed_int + 1
            end = len(nums) - 1

            while st < end:
                total = nums[fixed_int] + nums[st] + nums[end]
                if total < 0:
                    st += 1
                elif total > 0:
                    end -= 1
                else:
                    finl.append([nums[fixed_int], nums[st], nums[end]])
                    st += 1
                    end -= 1
                    
                    # Skip duplicates for the st and end pointers
                    while st < end and nums[st] == nums[st - 1]:
                        st += 1
                    while st < end and nums[end] == nums[end + 1]:
                        end -= 1
        return finl
        