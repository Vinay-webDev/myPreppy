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

#10 divisble by a or b in range 1 to n
n = 20
a = 2
b = 3
n2 = 30
a2 = 5
b2 = 7
class Solution:
    def divisble_by_a_or_b(self, n, a, b):
        for i in range(1, n + 1):
            if i % a == 0 or i % b == 0:
                print(i, end=" ")
# sol = Solution()
# sol.divisble_by_a_or_b(n, a, b) #2 3 4 6 8 9 10 12 14 15 16 18 20
# sol.divisble_by_a_or_b(n2, a2, b2) #5 7 10 14 15 20 21 25 28 30

#11. factors of num
num = 20
num2 = 30
class Solution:
    def factors(self, num):
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=" ")
# sol = Solution()
# sol.factors(num) #1 2 4 5 10 20
# sol.factors(num2) #1 2 3 5 6 10 15 30

#12 number of factors
num = 20
num2 = 30
class Solution:
    def no_of_factors(self, num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count
# sol = Solution()
# print(sol.no_of_factors(num)) #6
# print(sol.no_of_factors(num2)) #8

#13 check prime number
n = 1
n2 = 2
n3 = 3
n4 = 5
class Solution:
    def check_prime(self, n):
        #this will not return 1 as prime handles edge case for numbers less than 2
        if n < 2:
            return "Not a prime number"
        no_of_factors = 0 #prime has only 2 factors 1 and itself
        for i in range(1, n + 1):
            if n % i == 0:
                no_of_factors += 1
        
        if no_of_factors == 2:
            return "Prime number"
        else:
            return "Not a prime number"
# sol = Solution()
# print(sol.check_prime(n)) #Not a prime number
# print(sol.check_prime(n2)) #Prime number
# print(sol.check_prime(n3)) #Prime number
# print(sol.check_prime(n4)) #Prime number

#14 check prime another method
n = 1
n2 = 2
n3 = 3
n4 = 5
class Solution:
    def check_prime(self, n):
        no_of_factors = 0
        #handles edge case for numbers less than 2
        if n < 2:
            return "Not a prime number"

        for i in range(2, (n//2) + 1):
            if n % i == 0:
                no_of_factors += 1

        if no_of_factors == 0:
            return "Prime number"
        else:
            return "Not a prime number"
# sol = Solution()
# print(sol.check_prime(n)) #Not a prime number
# print(sol.check_prime(n2)) #Prime number
# print(sol.check_prime(n3)) #Prime number
# print(sol.check_prime(n4)) #Prime number

#15 check prime method 3
n = 1
n2 = 2
n3 = 3
n4 = 5
class Solution:
    def check_prime(self, n):
        #handles edge case for numbers less than 2
        if n < 2:
            return "Not a prime number"
        #we know that prime has only two factors 1 and itself
        for i in range(2, (n//2) + 1):
            if n % i == 0:
                return "Not a prime number"
        return "Prime number"
# sol = Solution()
# print(sol.check_prime(n))  #Not a prime number
# print(sol.check_prime(n2)) #Prime number
# print(sol.check_prime(n3)) #Prime number    
# print(sol.check_prime(n4)) #Prime number   

#16 check prime method 4
n = 1
n2 = 2
n3 = 3
n4 = 5
class Solution:
    def check_prime(self, n):
        if n < 2:
            return "Not a prime number"
        for i in range(2, int(n ** 0.5) + 1): #i*i <= n is same as i <= sqrt(n)
            if n % i == 0:
                return "Not a prime number"
        return "Prime number"
sol = Solution()
# print(sol.check_prime(n)) #Not a prime number
# print(sol.check_prime(n2)) #Prime number
# print(sol.check_prime(n3)) #Prime number
# print(sol.check_prime(n4)) #Prime number

#17 print all prime numbers between given two numbers
n1 = 10
n2 = 20
n3 = 50
n4 = 100
class Solution:
    def print_prime(self, n1, n2):
        def check_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        #make sure that "start" is less than "end"
        start, end = (n1, n2) if n1 < n2 else (n2, n1)
        for i in range(start, end + 1):
            if check_prime(i):
                print(i, end=" ")
# sol = Solution()
# sol.print_prime(n1, n2) #11 13 17 19
# sol.print_prime(n3, n4) #53 59 61 67 71 73 79 83 89 97

#18 Sum of all prime numbers up to n
# import math
n = 10
n2 = 20
n3 = 100
class Solution:
    def sum_of_prime(self, n):
        def check_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        total = 0

        for i in range(2, n + 1):
            if check_prime(i):
                total += i
        return total
# sol = Solution()
# print(sol.sum_of_prime(n))  #17
# print(sol.sum_of_prime(n2)) #77
# print(sol.sum_of_prime(n3)) #1060

#19 find the largest prime number in given range
# import math
n1 = 10
n2 = 20
n3 = 50
n4 = 100
class Solution:
    def largest_prime(self, n1, n2):
        def check_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        #start is always less than end
        start, end = (n1, n2) if n1 < n2 else (n2, n1)
        largest_prime_num = -1
        for i in range(start, end + 1):
            if check_prime(i):
                largest_prime_num = i
        return largest_prime_num
# sol = Solution()
# print(sol.largest_prime(n1, n2)) #19
# print(sol.largest_prime(n3, n4)) #97

#20 find the smallest prime number in given range
# import math
n1 = 10
n2 = 20
n3 = 50
n4 = 100
class Solution:
    def smallest_prime(self, n1, n2):
        def check_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5 ) + 1):
                if num % i == 0:
                    return False
            return True
        #start from small end large
        start, end = (n1, n2) if n1 < n2 else (n2, n1)
        for i in range(start, end + 1):
            if check_prime(i):
                return i
sol = Solution()
print(sol.smallest_prime(n1, n2)) #11
print(sol.smallest_prime(n3, n4)) #53

#21 Count prime numbers up to n that are divisible by a given number
n = 20
n2 = 50
n3 = 100





































#15 reverse a number
num = 12345
num2 = 2024
num3 = 100
class Solution:
    def reverse(self, num):
        reversed_num = 0

        while num > 0:
            digit = num % 10 #get the last digit
            reversed_num = reversed_num * 10 + digit # add the digit to reversed num
            num //= 10 #remove the last digit from num

        return reversed_num
# sol = Solution()
# print(sol.reverse(num)) #54321
# print(sol.reverse(num2)) #4202
# print(sol.reverse(num3)) #1



















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
