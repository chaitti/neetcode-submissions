class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1]*len(nums)
        left_arr[0] = nums[0]
        n=len(nums)
        for i in range(1,n):
            left_arr[i] = left_arr[i-1]*nums[i]
        right = 1
        for i in range(1,n):
            left_arr[n-i] = left_arr[n-i-1]*right
            right*=nums[n-i]
        left_arr[0]=right
        return left_arr

