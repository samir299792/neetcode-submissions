class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        X = []

        for i, num in enumerate(nums):
            X.append([num, i])

        X.sort()
        i=0
        j=len(nums)-1

        while i<j:
            sum = X[i][0] + X[j][0]
            if sum == target:
                return [min (X[i][1],X[j][1]), max(X[i][1], X[j][1])]

            if sum < target:
                i += 1
            else:
                j -= 1
        return []



        
