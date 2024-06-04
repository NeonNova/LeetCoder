class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevEles = {} # value : index

    #enumerate format is index, number 
        for i, n in enumerate(nums):
            diff = target - n 

            if diff in prevEles:
                #the indices of the 2 numbers are the index of the number found, ie i and its diff
                return [prevEles[diff], i]
            prevEles[n] = i
        return