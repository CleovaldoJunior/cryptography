import math
import random
import time
from hashlib import sha256


# Verificação se um número n >= 3 é primo
def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    while (a != 0):
        (a, b) = [b % a, a]
    return b


def extended_gcd(a, b):
    if (a >= 0 and b >= 0):
        (c, d) = (a, b)
        (uc, vc, ud, vd) = (1, 0, 0, 1)
        while c != 0:
            q = math.floor((d / c))
            (c, d) = (d - (q * c), c)
            (uc, vc, ud, vd) = (ud - (q * uc), vd - (q * vc), uc, vc)
        return d, (ud, vd)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def rsa_prime(k):
    r = 100 * k
    n = random.choice(list(range(2 ** (k - 1), (2 ** k) - 1)))
    while (r > 0):
        if ((n % 3) != 1 and (n % 5) != 1 and is_prime(n) == True):
            break
        n = random.choice(list(range(2 ** (k - 1), (2 ** k) - 1)))
        r = r - 1

    return n

def garners_formula(a, b, p, q):
    x = ((((a-b)*((1/q)%p))%p)*q) + b
    return int(x)

def generate_rsa_key(k, e, p = None, q = None):

    if(p == None and q == None):
        p = rsa_prime(math.floor((k / 2)))
        q = rsa_prime(math.floor((k / 2)))
    assert p != q, 'Q == P Error'

    t = ((p - 1) * (q - 1)) / gcd((p - 1), (q - 1))

    g, (u, v) = extended_gcd(3, t)
    assert g == 1
    d3 = u % t

    g, (u, v) = extended_gcd(5, t)
    assert g == 1
    d5 = u % t
    return p*q, int(d3), int(d5)


def encrypt_random_key_rsa(public_k):
    ##K = sha256(str(r).encode()).hexdigest()
    n = public_k[0]
    e = public_k[1]
    k = math.floor(math.log(n, 2))
    r = random.randrange(0, (2 ** k) - 1)
    c = (r ** e) % n
    return (c,r)

def encrypt_key_rsa(public_k, key_number):
    ##K = sha256(str(r).encode()).hexdigest()
    n = public_k[0]
    e = public_k[1]
    c = (key_number ** e) % n
    return (c)

def decrypt_key_rsa(private_k, c):
    #K = sha256(str((c ** (1 / e)) % n).encode()).hexdigest()
    n = private_k[0]
    d = private_k[1]
    plaintext = (c**d)%n
    return plaintext


def main(bits, number_key = None, p = None, q = None):
    assert 10 <= bits <= 25, 'Bit range error'
    if(p == None and q == None):
        p = rsa_prime(math.floor((bits / 2)))
        q = rsa_prime(math.floor((bits / 2)))
        print(p,q)
    assert q!=p, 'Q == P error'
    ###n = pq | ds = D Signature | d = D decryption
    e = 5
    n,ds,dd = generate_rsa_key(bits, e, p, q)
    public_key = (n,e)
    private_key = (n, dd)
    if(number_key == None):
        ciphertext,r = encrypt_random_key_rsa(public_key)
        print('Ciphertext =',ciphertext,'| key =',r)
    else:
        ciphertext = encrypt_key_rsa(public_key, number_key)
        print('Ciphertext =', ciphertext, '| key =', number_key)
    plaintext = decrypt_key_rsa(private_key, ciphertext)
    print('Recovered key:', plaintext)

def reset_primes(bits):
    p = rsa_prime(math.floor((bits / 2)))
    q = rsa_prime(math.floor((bits / 2)))
    return p, q

bits = 20

p,q = reset_primes(bits)

while(True):
    plainText = int(input())
    bits = plainText.bit_length()
    main(bits, plainText, p, q)







