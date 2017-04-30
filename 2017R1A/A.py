for T in range(input()):
    R,C=map(int,raw_input().split())
    M=[list(raw_input()) for r in range(R)]
    def solve(R1,R2,C1,C2):
        t='?'
        for r in range(R1,R2+1):
            for c in range(C1,C2+1):
                t=M[r][c]
                if t!='?':
                    for x in range(R1,r+1):
                        for y in range(C1,c+1):
                            M[x][y]=t
                    while r<R2 and all([M[r+1][x]=='?' for x in range(C1,c+1)]):
                        r+=1
                        for x in range(C1,c+1): M[r][x]=t
                    while c<C2 and all([M[x][c+1]=='?' for x in range(R1,r+1)]):
                        c+=1
                        for x in range(R1,r+1): M[x][c]=t
                    if r<R2: solve(r+1,R2,C1,c)
                    if c<C2: solve(R1,R2,c+1,C2)
                    return
    solve(0,R-1,0,C-1)
    print "Case #{}:".format(T+1)
    for m in M: print ''.join(m)
