for T in range(input()):
    D,N=map(int,raw_input().split())
    D=float(D)
    KS=[map(int,raw_input().split()) for n in range(N)]
    t=[(D-k)/s for k,s in KS]
    # print t,D/max(t)
    print "Case #{}: {:.6f}".format(T+1,D/max(t))
