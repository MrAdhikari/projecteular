#problem two

import math

def fibonacci_direct(n):
    if n <= 0:
        return "Input should be a positive integer."
    # Golden ratio
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    
    # Direct formula
    fib_n = (phi**n - psi**n) / math.sqrt(5)
    return round(fib_n)  # Round the result to get an integer


temp = 0
sum = 0
for i in range(25,35):
    while(fibonacci_direct(i) <= 4000000):
        temp =i

while(temp > 25):
    if (temp - 2) % 3 == 0:
        break
    temp -= 1

for i in range(1, temp+1):
    sum = sum + fibonacci_direct(i)

print(f'the sum is {sum}')