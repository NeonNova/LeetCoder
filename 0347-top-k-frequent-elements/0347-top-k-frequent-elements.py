class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        freq =[[] for i in range(len(nums)+1)]

        for n in nums:
            hm[n] += 1
        for n, c in hm.items():
            freq[c].append(n)
        #ie n occurs c times and we are updating that in the freq array

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        

        
        