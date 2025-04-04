#10001 prime

def is_prime(n):
    temp = 0
    for i in range(1,n):
        if n % i == 0:
            temp += 1
    return (temp==2)

i=1
temp = 0
while(temp != 10001):
    while(1):
        if is_prime(i):
            temp += 1
        i+=1
print(f"10001st prime is {i}")
    