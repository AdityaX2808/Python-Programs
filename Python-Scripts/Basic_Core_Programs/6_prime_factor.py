def prime_factors():
    n = int(input("Enter a number to find its prime factors: "))
    i = 2
    print("Prime factors:", end=" ")
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 1
    if n > 1:
        print(n)
