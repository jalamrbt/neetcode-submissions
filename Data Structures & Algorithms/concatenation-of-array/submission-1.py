class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1= nums
        for i in range(0,len(nums)):
            nums1.append(nums[i])
        return nums1
