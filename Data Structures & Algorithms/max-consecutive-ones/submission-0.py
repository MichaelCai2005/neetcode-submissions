class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        score = 0 
        for i in nums:
            if i == 1:
                count += 1
                print(count)
            else:
                score = max(score, count)
                count = 0
        return max(score, count)
