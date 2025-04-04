import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


'''
so this is problem 6
'''
count = 0
num = 1
while count < 10001:
    num += 1
    if is_prime(num):
        count += 1

print(f"10001st prime is {num}")
