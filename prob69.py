#problem 69

def gcd_calc(a,b):
    while(b!=0):
        a,b = b, a %b
    return a

max_value = 0
max_number = 0
for i in range(2, 1000001):
    count = 0
    for j in range(1,i):
        count = 0
        if gcd_calc(i, j):
            count += 1
    temp = i/count

    if temp > max_value:
        max_value = temp
        max_number = i
print(f"the number is {max_number}")
