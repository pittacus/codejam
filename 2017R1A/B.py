
for T in range(input()):
    N,P=map(int,raw_input().split())
    R=map(int,raw_input().split())
    Q=[map(int,raw_input().split()) for n in range(N)]
    import math
    S=[[(int(math.ceil(Q[n][p]/1.1/R[n])),int(math.floor(Q[n][p]/0.9/R[n]))) for p in range(P)] for n in range(N)]
    # if T+1!=30: continue
    # print '-'*10
    # print T+1,N,P,R,Q
    # for n in range(N):
    #     for p in range(P):
    #         print "{!r}".format(S[n][p]),
    #     print
    if N==1:
        max_count=len([s for s in S[0] if s[0]<=s[1]])
    elif N==2:
        # for p1 in range(P):
        #     for p2 in range(P):
        #         x=S[0][p1]
        #         y=S[1][p2]
        #         s=(max(x[0],y[0]),min(x[1],y[1]))
        #         print 1 if s[0]<=s[1] else 0,
        #     print
        import itertools
        max_count=0
        for p in itertools.permutations(range(P)):
            count=0
            for k in range(P):
                x=S[0][k]
                y=S[1][p[k]]
                s=(max(x[0],y[0]),min(x[1],y[1]))
                if s[0]<=s[1]: count+=1
            if count>max_count: max_count=count
    else:
        max_count=99999
    # print N,P
    # for n in range(N):
    #     print S[n]
    # V=[[0]*P for n in range(N)]
    # for s in solve(S,0,0,(0,10**7,V): print s;count+=1
    print "Case #{}: {}".format(T+1,max_count)
    #if T>30: break
