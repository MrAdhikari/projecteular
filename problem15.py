# #p15

# n = 20

# binary_list = (bin(i) for i in range(4**n +1) if (bin(i).count('1') == n) )

# print(sum(1 for _ in binary_list))

# # for x in binary_list:
# #     print(x)

import math

n = 20
result = math.comb(2 * n, n)
print(result)
