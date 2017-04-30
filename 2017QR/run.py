import sys

# 2017QR
# https://code.google.com/codejam/contest/3264486/dashboard

def A():
    #T=input()
    for t in range(input()):
    	S,K=raw_input().split()
        #print S,K
        K=int(K)
        S=[s=='+' for s in S]
        count=0
        for x in range(len(S)-K+1):
            if S[x]: continue
            count+=1
            for y in range(x,x+K):
                S[y]=not S[y]
        if all(S):
            print "Case #{}: {}".format(t+1,count)
        else:
            print "Case #{}: {}".format(t+1,'IMPOSSIBLE')

def B():
    def maxnum(n):
        return max(map(int,list(str(n))))
    def solve(n):
        if n<10: return n
        if maxnum(n//10)<=n%10:
            m=solve(n//10)
            if m==n//10:
                return m*10+n%10
            else:
                return m*10+9
        else:
            m=solve(n//10-1)
            return m*10+9
    for t in range(input()):
    	N=input()
        print "Case #{}: {}".format(t+1,solve(N))

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
D()
