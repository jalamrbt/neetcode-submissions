class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        done = False
        last = len(digits)-1
        while not done:
            if last<0:
                digits[0]=1
                digits.append(0)
                done= True
            elif digits[last]!=9:
                digits[last]+=1
                done=True
            else:   
                current = digits[last]
                digits[last]=0
                last-=1

        return digits