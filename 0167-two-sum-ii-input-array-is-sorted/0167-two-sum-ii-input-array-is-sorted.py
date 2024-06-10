class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st = 0 
        end = len(numbers)-1
        finl = [0,0]

        while st < end:
            if numbers[st] + numbers[end] > target:
                end -= 1
            elif numbers[st] + numbers[end] < target:
                st += 1
            else:
                finl[0] = st+1
                finl[1] = end+1
                return finl
                


        