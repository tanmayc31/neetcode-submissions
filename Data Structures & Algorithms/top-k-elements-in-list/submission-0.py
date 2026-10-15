class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i]= count.get(i, 0) + 1

        pairs = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [pair[0] for pair in pairs[:k]]
        