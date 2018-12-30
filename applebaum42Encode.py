#3-party CDS because reconstruction in odd-k will take time
#So 3 partitions
#For simplicity's sake, set n such that d | n; then len(Vi)=n//d for all i
#Map from each Vi to [N] -> just use position in list

from halp.undirected_hypergraph import UndirectedHypergraph
import secrets
import shamirEncode
import beimelOddEncode
import beimel3

def buildGraph():
    H = UndirectedHypergraph()
    node_delimiter = ','
    column_separator = ';'
    H.read('hypergraph.txt', node_delimiter, column_separator)
    return H

def partition(H):
    subG = []
    parts = []
    with open('partitions.txt', 'r') as fin:
        parts = fin.readlines()
    for line in parts:
        pns = line.strip().split(',')
        subG.append(pns)
    return subG

def split(mini, total, p, s):
    shares = shamirEncode.share(total, mini, p, s)
    return shares

def CDS(G, E, N, f, s0):
    gnum = len(G)
    a = dict()
    if gnum < 3:
        print('To be implemented...')
        return {}
    elif gnum == 3:
        #print('s0', s0)
        qbits = beimel3.randgen(N)
        rbits = beimel3.randgen(N)
        for i in range(gnum):
            for j in range(len(G[i])):
                v = int(G[i][j])
                #print(i, j)
                a[v] = beimel3.share(i+1, str(v % N), N, f, qbits, rbits, s0)
        return a
    elif (gnum % 2) == 1:
        kprime = (gnum - 1) // 2
        rbits = beimelOddEncode.randomness(N, gnum, kprime)
        #print('rbits', rbits)
        for i in range(gnum):
            for j in range(len(G[i])):
                v = int(G[i][j])
                a[v] = beimelOddEncode.share(i+1, str(v % N), rbits, N, gnum, kprime, f, s0)
        return a
    else:
        print('To be implemented...')
        return {}

def getEdges(H):
    print('Edges are')
    edgeIDs = H.get_hyperedge_id_set()
    E = []
    for item in edgeIDs:
        edge = H.get_hyperedge_nodes(item)
        print(edge)
        E.append(edge)
    return E

def allotShares(G, si, av, bv):
    #print(si)
    #print(av)
    #print(bv)
    gnum = len(G)
    ctr = 0
    sh = dict()
    for i in range(gnum):
        for v in G[i]:
            sh[v] = (si[i+1], av[int(v)], bv[int(v)-1])
            #if i==1:
             #   print('av', v, av[int(v)], sh[v][1])
    return sh

def execute():
    p = 19
    H = buildGraph()
    E = getEdges(H)
    nodes = H.get_node_set()
    G = partition(H) #for now, read partitions from a file; nodes as comma-separated strings/integers; one partition per line
    #add nodes not in any edge
    sublen = []
    for sub in G:
        for subnode in sub:
            if (subnode not in nodes):
                H.add_node(subnode)
        sublen.append(len(sub))
    nodes = H.get_node_set()
    n = len(nodes)
    t = len(G)
    s = secrets.randbits(1)
    #print('Encoding secret', s)
    N = max(sublen)
    M = N
    print('s', s, 'n', n, 't', t)

    f = dict()
    for edge in E:
        elst = []
        for v in edge:
            elst.append(int(v))
        elst = sorted(elst)
        newEdge = []
        for v in elst:
            vN = v % N
            vstr = str(vN)
            newEdge.append(vstr)
        estr = ','.join(newEdge)
        f[estr] = 1
    
    slist = split(t+1, t+1, p, s)
    #print('shamir', slist)
    s0 = slist[0][1]

    a = CDS(G, E, N, f, s0)

    b = split(t+1, n, p, s)

    shares = allotShares(G, slist, a, b)

    return t, N, shares, nodes, f

#execute()
