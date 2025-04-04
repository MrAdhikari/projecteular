#10001 prime

def is_prime(n):
    temp = 0
    for i in range(1,n):
        if n % i == 0:
            temp += 1
    return (temp==2)

i=1
pos = 0
while(pos != 10001):
    if is_prime(i):
        pos += 1
    i+=1
    
print(f"10001st prime is {i}")
    