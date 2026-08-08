class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        i=0
        result = []
        for number in nums:

            complement = target - number
            if complement in set:

                result = [set[complement],i]
                break
            set[number] = i
            i+=1
        return result

