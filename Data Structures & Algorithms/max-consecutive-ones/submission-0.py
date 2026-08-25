class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest=0
        current=0
        for digit in nums:
            if digit==1:
                current+=1
            elif digit==0:
                if current>longest:
                    longest = current
                current =0
        if current>longest:
            longest = current

        return longest