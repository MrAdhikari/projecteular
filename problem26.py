#problem 26



max_pos = 0
max_length = 0

for i in range(2,1000):
    count = 0
    r = 1
    d = 10
    seen = {}

    while r != 0 and r not in seen:
        seen[r] = count
        r = (r*10 % i)
        count +=1

    if r!= 0:
        length = count - seen[r]
    else:
        length = 0


    if length > max_length:
        max_length =length
        max_pos = i
    
print(f"The number is {max_pos}")