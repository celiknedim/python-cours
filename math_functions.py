import sys, math


def fib(n):
    print(f"fib({n})")
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)


def is_prime(N):
    
    divise = 0
    if N==0 or N==1:
        return False
    else:
        for i in range(2, int(math.sqrt(N))+1):
            if  N % i == 0:
                divise = 1
                return False
        if divise == 0:
            return True
        
# Nombres premiers jumeaux : Identifiez et affichez les paires de nombres 
# premiers jumeaux (deux nombres premiers dont la différence est de 2) 
# jusqu'à un certain nombre N ?

# def jumaux(n):
#     twins = []
#     for num in range(2, n):
#         if is_prime(num) and is_prime(num + 2):
            