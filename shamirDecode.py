def prod(lst):
    acc = 1
    for item in lst:
        acc = acc * item
    return acc

def invert(a, m):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while m != 0:
        quot = a // m
        a, m = m, a%m
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x

def recover_secret(coal, t, p):
    if len(set(coal)) >= t:
        x = 0
        nums = []
        dens = []
        k = len(coal)
        #print('coal', coal)
        for i in range(k):
            others = [index[0] for index in coal]
            #print('others', others)
            cur = others.pop(i)
            newnums = []
            newdens = []
            for o in others:
                #print('o', o)
                #print('cur', cur)
                newnums.append(x-int(o))
                newdens.append(cur-o)
            #print(others, newnums, newdens)
            nums.append(prod(newnums))
            dens.append(prod(newdens))
            #print(dens)
        den = prod(dens)
        num = 0
        for i in range(k):
            left = (nums[i] * den * coal[i][1]) % p
            right = invert(dens[i], p)
            num = num + (left * right)
        fin = ((num * invert(den, p)) + p) % p
        return fin
    else:
        print('Coalition too small.')
        return 0
#c = [(10,5), (11,2), (6,5), (9,12), (5, 15), (1,2), (15,7)]
#print(recover_secret(c, 5, 19))
