#problem 5

list1 = []
gcd = 1
product = 1

for i in range(1,21):
    list1.append(i)

def gcd_calculator(a,b):
    while(a != b):
        if b < a:
            a = a-b
        else:
            b = b-a
    return a

for i in range(21):
    gcd = gcd_calculator(gcd, i)
    product = product*i
    
print(f"The lcm is {product/gcd}")