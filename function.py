'''
def hello(name ='argument'):
    # return value
    print(f"blabla {name}")
hello('nedim')
hello()
'''

'''
burasi multiline
comment
kismi
'''



# # function recursive
# def fact(n):
#     if n<=1:
#         return 1
#     return n * fact(n-1)

# print(fact(10))

memo = {0:0, 1:1}
def fibo(memo, n):
    if n<=1:
        return n
    print(f"fibo{memo}, {n}")
    if n not in memo:
        memo[n] = fibo(memo, n-1) + fibo(memo, n-2)
    return memo[n]
print(fibo(memo, 9))