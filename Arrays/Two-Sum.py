class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s ={}

        for i, num in enumerate(nums):
            req = target - num

            if req in s:
                return [s[req],i]

            s[num] = i
