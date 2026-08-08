class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = set()

        found=False
        for item in nums:
            
            if item in nums2:
                found = True
            nums2.add(item)

        return found