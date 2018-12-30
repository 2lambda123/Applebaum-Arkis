from halp.undirected_hypergraph import UndirectedHypergraph
import shamirDecode
import beimelOddDecode
import beimel3

def reconstruct(k, N, shares, nodelist, f):
    p = 19
    if len(nodelist) == k:
        si = []
        cds = []
        shamir2 = []
        for item in nodelist:
            #print(item)
            #print(item, len(shares))
            sj = shares[item]
            cds.append(sj[1])
            si.append(sj[0])
            #print(cds)
            shamir2.append(sj[2])
            #print(item, sj)
        auth = [str(int(v)%N) for v in nodelist]
        #print(cds)

        nodestr = ','.join(auth)
        if len(nodelist) > 3:
            s0 = beimelOddDecode.decode(cds, f, nodestr, k, N)
            #print('s0', s0)
        else:
            s0 = beimel3.reconstruct(cds[0], cds[1], cds[2], nodestr)

        slist = [(1, int(s0))] + list(set(si))
        #print('slist', slist)

        s = shamirDecode.recover_secret(slist, k, p)
        print('Secret is', s)
        return s
        
    elif len(nodelist) > k:
        shamir2 = []
        for item in nodelist:
            shamir2.append(shares[item][2])

        s = shamirDecode.recover_secret(shamir2, k+1, p)
        print('Secret is', s)
        return s

    else:
        print('Coalition too small; secret cannot be recovered.')




