import math
import random

#Verificação se um número n >= 3 é primo
def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    

    return True

#Numero primo de grande escala
def largePrimes(Lb,Ub):
    if(Lb<= 2 or Lb > Ub):
        return (-1)

    num = list(range(Lb, Ub))

    r = 100*((math.floor(math.log(Ub, 2)))+1)

    n = random.choice(num)

    while(is_prime(n) == False):
        if(r <= 0):
            break
        r -= 1
        n = random.choice(num)

    return(n)

def rsa_prime(k):
    r = 100*k
    n = random.choice(list(range(2**(k-1), (2**k)-1)))
    while(r > 0):
        if((n%3) != 1 and (n%5) != 1 and is_prime(n) == True):
            break
        n = random.choice(list(range(2**(k-1), (2**k)-1)))
        r = r-1
        
    return n


#Teorema do Resto Chines
def trs_um(x, p, q):
    a = x%p
    b = x%q
    return a,b
        
def trs_dois(x, y, p = largePrimes(3, 500), q = largePrimes(3, 500), e = 'soma'):

    if e == 'soma':
            print('Soma:')
            r = ((x%p) + (y%p))%p
            s = ((x%q) + (y%q))%q
            (a,b) = (r,s)
            return(a,b)
        
    elif e == 'mult':
            print('Mult:')
            r = ((x%p)*(y%p))%p
            s = ((x%q)*(y%q))%q
            (a,b) = (r,s)
            return(a,b)
        
def garners_formula(a, b, p, q):
    x = ((((a-b)*((1/q)%p))%p)*q) + b
    return int(x)
