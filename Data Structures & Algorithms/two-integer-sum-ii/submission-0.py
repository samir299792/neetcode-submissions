class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using a two pointer approach
        X = []
        for i, num in enumerate(numbers):
            X.append([num, i])
        
        i, j = 0, len(numbers)-1

        while i<j:
            sum = X[i][0] + X[j][0]

            if sum == target: 
                return [min(X[i][1],X[j][1]) + 1, max(X[i][1],X[j][1]) + 1]

            if sum < target:
                i += 1
            else:
                j -= 1
        
        return []