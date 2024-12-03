#1 find the whether the number is even or odd
num1 = 33
num2 = 32
num3 = 100

class Solution:
    def even_odd(self, num):
        if (num % 2 == 0):
            return "even"
        else:
            return "odd"

# sol = Solution()
# print(sol.even_odd(num1)) #odd
# print(sol.even_odd(num2)) #even
# print(sol.even_odd(num3)) #even

#2 print the digit that is in unit place of the number
num1 = 123
num2 = 38
num3 = 28393982
class Solution:
    def last_digit(self, num):
        return num%10

# sol = Solution()
# print(sol.last_digit(num1)) #3
# print(sol.last_digit(num2)) #8
# print(sol.last_digit(num3)) #2

#3 max of Two num
a = 100
b = 200
a2 = 500
b2 = 900
class Solution:
    def max_of_two(self, a, b):
        if a > b:
            return a
        else:
            return b
# sol = Solution()
# print(sol.max_of_two(a, b)) #200
# print(sol.max_of_two(a2, b2)) #900

#4 max of four number
num1 = 100
num2 = 200
num3 = 300
num4 = 400
class Solution:
    def max_of_four(self, num1, num2, num3, num4):
        max = num1
        if num2 > max:
            max = num2
        if num3 > max:
            max = num3
        if num4 > max:
            max = num4
        return max
# sol = Solution()
# print(sol.max_of_four(num1, num2, num3, num4)) #400

#5. swap two variables (using temp⚠️)
a = 100
b = 200
a2 = "bro"
b2 = "hello"
class Solution:
    def swap(self, a, b):
        temp = a
        a = b
        b = temp
        print(a, b)
# sol = Solution()
# sol.swap(a, b)  # 200 100
# sol.swap(a2, b2) # hello bro

#6 swap without using temp variable
a = 100
b = 200
a2 = 500
b2 = 300
class Solution:
    def swap_without_temp(self, a, b):
        a = a + b
        b = a - b
        a = a - b
        print(a, b)
# sol = Solution()
# sol.swap_without_temp(a, b)  # 200 100
# sol.swap_without_temp(a2, b2)  # 300 500

#7 check for num that ends with zero
num = 123
num2 = 1000
class Solution:
    def end_with_zero(self, num):
        if num % 10 == 0:
            return True
        else:
            return False
# sol = Solution()
# print(sol.end_with_zero(num))  #False
# print(sol.end_with_zero(num2)) #True

#8 sum of digits (converting num to string approach⚠️)
num = 12345
num2 = 99999
num3 = 2024
class Solution:
    def sum_of_digits(self, num):
        total = 0
        for digit in str(num):
            total += int(digit)
        return total
# sol = Solution()
# print(sol.sum_of_digits(num))  #15
# print(sol.sum_of_digits(num2)) #45
# print(sol.sum_of_digits(num3)) #8

#9 sum of digits without converting num to string
num = 12345
num2 = 99999
num3 = 2024
class Solution:
    def sum_of_digits(self, num):
        total = 0
        while num > 0:
            total += num % 10 #get last digit
            num //= 10        #remove last digit
        return total
# sol = Solution()
# print(sol.sum_of_digits(num))
# print(sol.sum_of_digits(num2))
# print(sol.sum_of_digits(num3))

#10 































#n. Pairs sum up to the target Two Pointers in py
array1 = [1, 39, 8, 3, 7]
target1 = 10
array2 = [20, 1, 38, 10]
target2 = 30
class Solution:
    def two_pointers(self, arr, target):
        arr.sort()
        left = 0
        right = len(arr) - 1

        while (left < right):
            sum = arr[left] + arr[right]
            if (sum == target):
                return [arr[left], arr[right]]
            elif (sum < target):
                left = left + 1
            else:
                right = right - 1

        return -1

# sol = Solution()
# print(sol.two_pointers(array1, target1))
# print(sol.two_pointers(array2, target2))
