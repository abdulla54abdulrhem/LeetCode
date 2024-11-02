class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        lastUnique = nums[0]
        
        changePlace = 1
        for i in range(1,len(nums)):
            if lastUnique != nums[i]:
                nums[changePlace] = nums[i]
                lastUnique = nums[i]
                changePlace += 1
        return changePlace
