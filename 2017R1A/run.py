import sys

# 2017R1A
# https://code.google.com/codejam/contest/5304486/dashboard

def A():
    # def solve(M):
    #     R=len(M)
    #     C=len(M[0])
    #     for r in range(R):
    #         for c in M[r]:
    #             if M[r][c]=='?':
    #                 if r<R-1:
    for T in range(input()):
    	R,C=map(int,raw_input().split())
        M=[list(raw_input()) for r in range(R)]
        # global count
        # count=0
        def solve(R1,R2,C1,C2):
            # global count
            # count+=1
            # if count>11: return
            # print 'A',R1,R2,C1,C2
            # for m in M: print ''.join(m)
            #import os
            #os.system("pause")
            # for r in range(R1,R2+1):
            #     for c in range(C1,C2+1):
            #         print M[r][c],
            #     print
            t='?'
            for r in range(R1,R2+1):
                for c in range(C1,C2+1):
                    t=M[r][c]
                    if t!='?':
                        r1=R1;c1=C1
                        for x in range(r1,r+1):
                            for y in range(c1,c+1):
                                M[x][y]=t
                        # print '#',r1,c1,r,c
                        r2=r;
                        while r2<R2 and all([M[r2+1][x]=='?' for x in range(C1,c+1)]):
                            r2+=1
                            for x in range(C1,c+1): M[r2][x]=t
                        c2=c
                        while c2<C2 and all([M[x][c2+1]=='?' for x in range(R1,r2+1)]):
                            c2+=1
                            for x in range(R1,r2+1): M[x][c2]=t
                        # print 'B',R2+1,r2,C1,C2
                        # print 'B',R1,r2,C2+1,c2
                        if r2<R2: solve(r2+1,R2,C1,c2)
                        if c2<C2: solve(R1,R2,c2+1,C2)
                        return
        # if T!=4: continue
        solve(0,R-1,0,C-1)
        print "Case #{}:".format(T+1)
        for m in M: print ''.join(m)

def B():
    for T in range(input()):
    	N,P=map(int,raw_input().split())
        R=map(int,raw_input().split())
        Q=[map(int,raw_input().split()) for n in range(N)]
        import math
        S=[[(int(math.ceil(Q[n][p]/(R[n]*1.1))),int(math.floor(Q[n][p]/(R[n]*0.9)))) for p in range(P)] for n in range(N)]
        for n in range(N):
            print S[n]
        M=[[0]*P for n in range(N)]
        if N==1:
            count=len(x for x in S[0] if x[0]<=x[1])
        if N==2:
            M={}
            for x in range(P):
                M[x]=set()
                for y in range(P):
                    sx=S[0][x]
                    sy=S[1][y]
                if sx[0]<=sy[1] and sx[1]>=sy[0]:
                    M[x].add(y)
            count=0
            while M:
                s=sorted([(len(M[x]),x) for x in range(P) if len(M[x])>0])
                if not s: break
                count+=1
                x=s[0][1]
                y=M[x].pop()
                M.pop(x)
                M.pop(y)
                for t in range(P):
                    if t not in M: continue
                    if x in M[t]: M[t].remove(x)
                    if y in M[t]: M[t].remove(y)
        print "Case #{}: {}".format(T+1,count)

def C():
    def solve(n,k):
        s=[n]
        while k:
            s.sort()
            r=s.pop()-1
            if r%2:
                s.append(r//2+1)
                s.append(r//2)
            else:
                s.append(r//2)
                s.append(r//2)
            k-=1
        return s[-2:]
    def solve2(N,K):
        #print "#", N,K
        if K==1: return [(N-1)//2+(N-1)%2, (N-1)//2]

        k=1
        while k<=K:
            k<<=1
        k>>=1

        N=N-k+1
        p=K-k
        #print "#", k,N,p

        A=N//k
        B=N%k
        C=A+1 if p<B else A
        #print "#", A,B,C
        C=C-1
        return [C//2+C%2,C//2]
    for t in range(input()):
    	N,K=map(int,raw_input().split())
        y,z=solve2(N,K)
        print "Case #{}: {} {}".format(t+1,y,z)


def D():
    for t in range(input()):
    	N,M=map(int,raw_input().split())
        A=[-1]*N
        B=[-1]*(2*N-1)
        P=['.']*N*N
        Q=['.']*N*N

        for m in range(M):
            x,r,c=raw_input().split()
            r=int(r)-1
            c=int(c)-1
            if x=='x' or x=='o': A[r]=c
            if x=='+' or x=='o': B[r+c]=r-c+N-1
            P[r*N+c]=x

        BS={}
        for r in range(N):
            for c in range(N):
                if r+c not in BS: BS[r+c]=set()
                BS[r+c].add(r-c+N-1)
        #print BS
        C=list(set(range(N)).difference(set([A[r] for r in range(N) if A[r]>0])))
        for r in range(N):
            if A[r]<0: A[r]=C.pop()
        #print A
        C=set(range(2*N-1)).difference(set([B[r] for r in range(2*N-1) if B[r]>0]))
        while True:
            rs=sorted([(len(C.intersection(BS[r])),r) for r in range(2*N-1) if B[r]<0 and C.intersection(BS[r])])
            #print "rs",rs
            if rs and rs[0][0]:
                r=rs[0][1]
                B[r]=C.intersection(BS[r]).pop()
                C.remove(B[r])
            else:
                break
        #print B

        score=0
        ndiff=0
        for r in range(N):
            for c in range(N):
                if A[r]==c and B[r+c]==r-c+N-1: Q[r*N+c]='o';score+=2
                elif A[r]==c: Q[r*N+c]='x';score+=1
                elif B[r+c]==r-c+N-1: Q[r*N+c]='+';score+=1

                if P[r*N+c]!=Q[r*N+c]: ndiff+=1

        print "Case #{}: {} {}".format(t+1,score,ndiff)

        for r in range(N):
            for c in range(N):
                if P[r*N+c]!=Q[r*N+c]:
                    print Q[r*N+c],r+1,c+1

        # for r in range(N):
        #     for c in range(N):
        #         print Q[r*N+c],
        #     print
        #pr(Smax)
        #pr(S)
        #break
A()
