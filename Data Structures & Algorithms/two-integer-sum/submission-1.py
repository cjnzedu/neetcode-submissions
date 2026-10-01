class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            rem = target - nums[i] 
            if rem not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap.get(rem), i]
        