#problem5

def gcd_calculator(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd_calculator(a, b)

lcm_result = 1
for i in range(1, 21):
    lcm_result = lcm(lcm_result, i)

print(f"The LCM of numbers from 1 to 20 is {lcm_result}")