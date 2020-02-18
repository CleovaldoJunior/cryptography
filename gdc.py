def gcd(a,b):
    while(a!= 0):
        (a,b)=[b%a,a]
    return b

def lcm(a,b):
    return (a*b)/gcd(a,b)

print(gcd(91261,117035))
        
