"""Frequency"""
"""1.calculate the frequency of an array"""
nums1 = [2,2,1,1,1,3,3,4,4]
nums2 = [5,5,5,6,7,8]
class Solution:
    def calculateFrequency(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        return frequency
sol = Solution()
print(sol.calculateFrequency(nums1))
#{2: 2, 1: 3, 3: 2, 4: 2}    
print(sol.calculateFrequency(nums2))
#{5: 3, 6: 1, 7: 1, 8: 1}
""""""""""""""""""""""""""""""""""""""""""""""""
class Solution:
    def calculateFrequency(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        return [value for value in frequency]
sol = Solution()
print(sol.calculateFrequency(nums1))  #[2, 1, 3, 4]
print(sol.calculateFrequency(nums2))  #[5, 6, 7, 8]

