nums1 = [8,1,2,3,6,-1,9,11,5,7]
queries1 = [[1,4],[6,8],[4,9],[8,9],[3,7]]
#1.how to calculate prefix sum👇
class Solution:
    def prefixSum(self, nums, queries):
        n = len(nums)
        p = [0] * n
        p[0] = nums[0]
        for i in range(1, n):
            p[i] = p[i - 1] + nums[i]
        return p
sol = Solution()
print(sol.prefixSum(nums1, queries1)) #[8, 9, 11, 14, 20, 19, 28, 39, 44, 51]











