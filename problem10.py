# Define the size limit
limit = 2000000

# Create a boolean list where index represents if the number is prime.
# Initially, set all entries to True.
is_prime = [True] * limit

# 0 and 1 are not primes, so set them to False.
is_prime[0] = is_prime[1] = False

# Use the Sieve of Eratosthenes algorithm to mark non-prime numbers.
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        # Mark all multiples of i as non-prime.
        for j in range(i * i, limit, i):
            is_prime[j] = False

# Sum up the primes below the limit.
prime_sum = sum(i for i, prime in enumerate(is_prime) if prime)
print(prime_sum)
