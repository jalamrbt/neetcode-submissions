class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index =-1
        left =0
        right = len(nums)-1
        while left<=right:
            middle = left+(right-left)//2
            if nums[middle] ==target:
                index = middle
                break
            elif nums[middle]<target:
                left =middle+1
            elif nums[middle]>target:
                right = middle-1
            

        return index