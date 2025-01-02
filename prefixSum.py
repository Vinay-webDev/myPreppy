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
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Solution:
    def prefixSum(self, nums, queries):
        n = len(nums)
        p = [0] * n
        for i in range(1, n):
            p[i] = p[i - 1] + nums[i]
        res = []
        for j in range(len(queries)):
            l = queries[j][0]
            r = queries[j][1]
            range_sum = p[r] - p[l - 1]
            res.append(range_sum)
        return res
sol = Solution()
print(sol.prefixSum(nums1, queries1)) #[12, 25, 37, 12, 28]
"""
a = []
range = [[l, r]]
to find sum between a given range(l, r)
range sum[l, r] = p[r] - p[l - 1]
but if l = 0 this would give [-1] so this is problem!
to fix this have one additional maybe 0 at 0 index of p[] array i,e.. prefix sum array
p = [0] * n + 1
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]
range formula ===>> sum[l, r] = p[r + 1] - p[l]
"""
"""if l can be 0 """
nums2 = [10,20,30,40,50]
queries2 = [[0,2],[0,4],[4],[1,3]]
class Solution:
    def prefixSum(self, nums, queries):
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(1, n + 1):
            p[i] = p[i - 1] + nums[i - 1]
        res = []
        for j in range(len(queries)):
            l = queries[j][0]
            r = queries[j][1]
            range_sum = p[r + 1] - p[l]
            res.append(range_sum)
        return res
sol = Solution()
print(sol.prefixSum(nums2, queries2)) #error because of this query ===> [4] where r = queries[j][1] is out of range

        








