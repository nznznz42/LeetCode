class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for index, value in enumerate(nums):
            diff = target-value

            if diff in visited:
                return [visited[diff], index]
            visited[value] = index
            
        return []
