'''
Problem 15 (inefficient)
'''

# n = 20

# binary_list = (bin(i) for i in range(4**n +1) if (bin(i).count('1') == n) )

# print(sum(1 for _ in binary_list))

# # for x in binary_list:
# #     print(x)


'''
problem 15
'''
# import math

# n = 20
# result = math.comb(2 * n, n)
# print(result)


'''
problem 16
'''

# n = 2 ** 1000
# sum = 0
# while(n > 0):
#     sum = sum + n % 10
#     n //= 10

# print(sum)

'''
Problem 20
'''

import math

n = math.factorial(100)
sum = 0
while(n > 0):
    sum = sum + n % 10
    n //= 10

print(sum)