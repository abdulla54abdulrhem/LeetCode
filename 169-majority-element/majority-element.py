class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key_count = {}
        for x in nums:
            if x in key_count:
                key_count[x] += 1
            else:
                key_count[x] = 1
        
        
        ans = nums[0]
        maxCount = key_count[nums[0]]
        for x in key_count.items():
            if maxCount < x[1]:
                ans = x[0]
                maxCount = x[1]

        return ans
            