class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # value -> index

        for i,n in enumerate(nums):  # index, number
            hash_map[n] = i
        # for key, value in hash_map:

        for i, n in enumerate(nums):
            difference = target - n
            if difference in hash_map and hash_map[difference] != i:
                return [i, hash_map[difference]]
        return []
