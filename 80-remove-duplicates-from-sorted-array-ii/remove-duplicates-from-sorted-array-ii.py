class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        distinct = nums[0]
        indexToChange = 1
        for i in range(1,len(nums)):
            
            if nums[i] == distinct and counter < 2:
                counter+=1
                nums[indexToChange] = nums[i] 
                indexToChange += 1

            elif distinct != nums[i]:
                counter = 1
                nums[indexToChange] = nums[i]
                distinct = nums[i]
                indexToChange += 1

        return indexToChange

                