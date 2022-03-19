def binom(n,k,p):
    prod = 1
    for i in range(k):
        prod = (prod * (n-i)) // (i+1) %p
    return prod
#Enlever le p et mod p pour sans modulo
