class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        array = []

        for num, count in hashmap.items():
            array.append([count, num])
        array.sort()

        result = []

        while len(result) < k:
            result.append(array.pop()[1])

        return result