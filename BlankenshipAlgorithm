def blankinship(a,b, verbose=False):
    arow = [a,1,0]
    brow = [b,0,1]
    if verbose:
        print(arow)
    while brow[0] != 0:
        q,r = divmod(arow[0], brow[0])
        if verbose:
            print(brow,q)
        if r == 0:
            break
        rrow =[r, arow[1]-q*brow[1], arow[2]-q*brow[2]]
        arow = brow
        brow = rrow
    return brow[0], brow[1], brow[2]


g,x,y = blankinship(65536,18199,True)
print(g, x,y)