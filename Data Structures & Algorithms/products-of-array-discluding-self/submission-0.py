class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length
        ans[0] = 1

        for i in range(1, length):
            ans[i] = ans[i-1] * nums[i-1]

        curr = 1

        for i in reversed (range(length)):
            ans[i] = curr * ans[i]
            curr = curr * nums[i]
        
        return ans