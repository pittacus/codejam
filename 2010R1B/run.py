import sys

# Round 1B 2010
# https://code.google.com/codejam/contest/635101/dashboard#s=p0

def A():
	def solve(NP,MP):
		H={}
		for p in NP:
			C=H
			for d in p.strip('/').split('/'):
				if d not in C: C[d]={}
				C=C[d]
		s=0
		for p in MP:
			C=H
			for d in p.strip('/').split('/'):
				if d not in C:
					C[d]={}
					s+=1
				C=C[d]
		return s

	T=int(input())
	for t in range(T):
		N,M=map(int,sys.stdin.readline().strip().split())
		NP=[sys.stdin.readline().strip() for n in range(N)]
		MP=[sys.stdin.readline().strip() for m in range(M)]
		s=solve(NP,MP)
		print "Case #{}: {}".format(t+1,s)

def B():
	def solve(X,Y,B,K):
		N=len(X)
		s=[len([t for t in range(k+1,N) if Y[t]<B]) for k in range(N) if Y[k]>=B]
		if len(s)<K: return 'IMPOSSIBLE'
		return sum(sorted(s)[:K])

	C=int(input())
	for c in range(C):
		N,K,B,T=map(int,sys.stdin.readline().strip().split())
		X=map(int,sys.stdin.readline().strip().split())
		V=map(int,sys.stdin.readline().strip().split())
		Y=[X[k]+V[k]*T for k in range(N)]
		s=solve(X,Y,B,K)
		print "Case #{}: {}".format(c+1,s)

def C():
	def solve(N):
		C=[[0 for x in xrange(N+1)] for y in xrange(N+1)]
		for x in xrange(0,N+1):
			C[x][0]=1
			C[x][x]=1
			for y in xrange(1,x):
				C[x][y]=C[x-1][y-1]+C[x-1][y]
		#print C
		M=[[0 for x in xrange(N+1)] for y in xrange(N+1)]
		for x in xrange(N+1): M[x][1]=1
		for x in xrange(3,N+1):
			for y in xrange(2,x):
				s=[M[y][t]*C[x-y-1][y-t-1] for t in xrange(1,y)]
				M[x][y]=sum(s)
				#print [(x,y,M[x][y],t,(y-t-1,x-y-1),C[x-y-1][y-t-1],M[y][t]) for t in xrange(1,y)]  #*C[y-t-1][x-y-1)
		#print M[N]
		return sum(M[N])

	def build(N):
		N=500
		C=[[0 for x in xrange(N+1)] for y in xrange(N+1)]
		for x in xrange(0,N+1):
			C[x][0]=1
			C[x][x]=1
			for y in xrange(1,x):
				C[x][y]=(C[x-1][y-1]+C[x-1][y])%100003
		#print C
		M=[[0 for x in xrange(N+1)] for y in xrange(N+1)]
		for x in xrange(N+1): M[x][1]=1
		for x in xrange(3,N+1):
			for y in xrange(2,x):
				s=[M[y][t]*C[x-y-1][y-t-1] for t in xrange(1,y)]
				M[x][y]=sum(s)%100003
				#print [(x,y,M[x][y],t,(y-t-1,x-y-1),C[x-y-1][y-t-1],M[y][t]) for t in xrange(1,y)]  #*C[y-t-1][x-y-1)
		return M

	M=build(500)
	for t in range(input()):
		n=int(input())
		s=sum(M[n])%100003
		#s=solve(int(input()))
		print "Case #{}: {}".format(t+1,s)

C()
