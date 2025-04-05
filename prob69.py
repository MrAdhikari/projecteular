# #problem 69


# '''
# Prime stuff
# '''
# prime_list = [True]*1000001
# prime_list[0] = False
# prime_list[1] = False
# prime_list[2] = True
# prime_list[3] = True

# for i in range(2, 1000001):
#     if prime_list[i] == True:
#         for j in range(2*i, 1000001, i):
#             prime_list[j] = False

# def gcd_calc(a,b):
#     while b!=0:
#         a,b = b, a %b
#     return a

# max_value = 0
# max_number = 0


# for i in range(2, 1000001):
#     if prime_list[i] == False:
#         count = 0
#         for j in range(1,i):
#             if gcd_calc(i, j) == 1:
#                 count += 1
#         temp = i / count

#         if temp > max_value:
#             max_value = temp
#             max_number = i
# print(f"the number is {max_number}")


MAX = 1000001
phi = list(range(MAX))  # initialize phi[i] = i

for i in range(2, MAX):
    if phi[i] == i:  # i is prime
        for j in range(i, MAX, i):
            phi[j] -= phi[j] // i

max_ratio = 0
max_number = 0

# Check only composite numbers (phi(n) for primes is n-1, giving a ratio ~ n/(n-1) which is near 1)
for i in range(2, MAX):
    if phi[i] == i - 1:  # i is prime (special case, except 2 where ratio = 2/1 = 2)
        continue
    ratio = i / phi[i]
    if ratio > max_ratio:
        max_ratio = ratio
        max_number = i

print(f"The number with the maximum n/phi(n) ratio is {max_number}")
