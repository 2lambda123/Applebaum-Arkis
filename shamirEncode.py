#TODO:
#Integrate with applebaum42
#Make p the next prime number above n 

import secrets

def genpoly(p, t, s):
    f = [s]
    for i in range(t-1):
        ai = secrets.randbelow(p)
        f.append(ai)
    return f

def evaluate(x, f, t, p):
    res = f[0]
    for j in range(1, t):
        xi = (f[j] * (x ** j)) % p
        res = (res + xi) % p
    return res

def share(n, t, p, s):
    f = genpoly(p, t, s)
    shares = []
    for i in range(1, n+1):
        bi = evaluate(i, f, t, p)
        shares.append((i,bi))
    return shares
