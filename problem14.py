
#problem 14 longest collatz


def collatz_counter(n):
    temp = 0

    if n == 4:
        return 3
    elif n ==2:
        return 2
    elif n == 1:
        return 1
    
    while n!=1:
        if n % 2 == 1:
            n = (3*n + 1)/2
            temp += 2
        else:
            n /= 2
            temp += 1
    return temp

collatz = [0]*1000001
max_length = 0
max_number = 1

# collatz[0] = 0
collatz[1] = 1 

for i in range(2, 1000001):
    if i % 2 == 0:
        collatz[i] = collatz[i // 2] + 1
    else:
        collatz[i] = collatz_counter(i)

    if collatz[i] > max_length:
        max_length = collatz[i]
        max_number = i

print(f"the largest is {max_number} and its length is {max_length}")






