#problem two

import math

def fibonacci_direct(n):
    n = n+1
    if n <= 0:
        return "Input should be a positive integer."
    # Golden ratio
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    
    # Direct formula
    fib_n = (phi**n - psi**n) / math.sqrt(5)
    return round(fib_n)  # Round the result to get an integer


temp = 32
sum = 0

# for i in range(1, temp+1):
#     sum = sum + fibonacci_direct(2+(3*(i-1)))

# print(f'the sum is {sum}')

for i in range(1, temp+1):
    if (i-2) % 3 == 0:
        # print(f"i is {i}")
        # print(fibonacci_direct(i))
        sum += fibonacci_direct(i)

print(sum)