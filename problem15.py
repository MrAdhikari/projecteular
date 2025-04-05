#p15

def square_path(n):
    if n == 1:
        return 2
    else:
        return 2*square_path(n-1) + 2*(n-1)
    
print(square_path(20))