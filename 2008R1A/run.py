import sys

# Round 1A 2008
# https://code.google.com/codejam/contest/32016/dashboard#s=p0

def A():
	def solve(P,Q):
		s=0
		for x,y in zip(sorted(P),reversed(sorted(Q))): s+=x*y
		return s

	N=int(input())
	for n in range(N):
		L=int(input())
		P=map(int,sys.stdin.readline().strip().split())
		Q=map(int,sys.stdin.readline().strip().split())
		s=solve(P,Q)
		print "Case #{}: {}".format(n+1,s)

def B():
	def solve(p,S):
		while True:
			succ=True
			for s in S:
				if not any([p[c[0]]==c[1] for c in s]):
					c=filter(lambda x:x[1], s)
					if c:
						p[c[0][0]]=1
						succ=False
						break
					else:
						return ['IMPOSSIBLE']
			if succ: return p

	N=int(input())
	for n in range(N):
		L=int(input())
		M=int(input())
		makeset=lambda s:set(zip(map(lambda x:x-1,s[::2]),s[1::2]))
		S=[makeset(map(int,sys.stdin.readline().strip().split())[1:])
		 	for m in range(M)]
		p=solve([0]*L,S)
		print "Case #{}: {}".format(n+1," ".join(map(str,p)))

def C():
	def solve(M):
		import math
		a,b=1,(3+math.sqrt(5))
		for m in xrange(M):
			a,b=b,(6*b-4*a)%1000
		return math.floor(a)
	def solve2(M):
		import math
		def matmul(x,y):
			return [
			(x[0]*y[0]+x[1]*y[2])%1000,
			(x[0]*y[1]+x[1]*y[3])%1000,
			(x[2]*y[0]+x[3]*y[2])%1000,
			(x[2]*y[1]+x[3]*y[3])%1000
			]
		S=[1,0,0,1]
		H=[6,-4,1,0]
		m=M-1
		while m:
			if m%2==1:
				S=matmul(S,H)
			H=matmul(H,H)
			#H=map(lambda x:x%1000, H)
			m/=2
		return math.floor((S[0]*6+S[1]*2)%1000-1)
	N=int(input())
	for n in range(N):
		M=int(input())
		#s=solve(M)
		s=solve2(M)
		print "Case #{}: {:0>3.0f}".format(n+1,s)

C()
