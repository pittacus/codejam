import sys

# Qualification Round 2009
# https://code.google.com/codejam/contest/90101/dashboard#s=p0

def A():
	def solve(L,P,M):
		def parse(P):
			s=[]
			ps=None
			for p in P:
				if p=='(':
					ps=[]
				elif p==')':
					s+=[ps]
					ps=None
				elif ps==None:
					s+=[p]
				else:
					ps+=[p]
			#print L,P,s
			return s
		P=parse(P)
		S=None
		for k,p in enumerate(P):
			sp=set()
			for s in p:
				 if (k,s) in M:
					sp.update(M[(k,s)])
			if S==None:
				S=sp
			else:
				S.intersection_update(sp)
			#print k,p,sp,S
		return len(S)

	L,D,N=map(int,sys.stdin.readline().strip().split())

	M={}
	for d in range(D):
		S=sys.stdin.readline().strip()
		for k,s in enumerate(S):
			if (k,s) in M:
				M[(k,s)].add(d)
			else:
				M[(k,s)]=set([d])
	import re
	for n in range(N):
		P=sys.stdin.readline().strip()
		s=solve(L,P,M)
		print "Case #{}: {}".format(n+1,s)

def B():
	def solve(M):
		H=len(M)
		W=len(M[0])
		L=[[None for y in xrange(W)] for x in xrange(H)]
		LP=range(H*W)
		#for label in list('abcdefghijklmnopqrstuvwxyz'):
		index=0
		for t in range(H*W):
			x,y=t/W,t%W
			if L[x][y]==None:
				while True:
					if L[x][y]==None:
						L[x][y]=index
					else:
						LP[index]=LP[L[x][y]]
					n=(x-1,y) if x>0 else None
					w=(x,y-1) if y>0 else None
					e=(x,y+1) if y<len(M[0])-1 else None
					s=(x+1,y) if x<len(M)-1 else None
					Z=[M[d[0]][d[1]] for d in [n,w,e,s] if d]
					if not Z: break
					zmin=min(Z)
					if M[x][y]<=zmin: break
					x,y=[d for d in [n,w,e,s] if d and M[d[0]][d[1]]==zmin][0]
				index+=1
		chrmap={v:chr(ord('a')+k) for k,v in enumerate(sorted(list(set(LP[:index]))))}
		for t in range(H*W):
			x,y=t/W,t%W
			L[x][y]=chrmap[LP[L[x][y]]]
		return L

	N=int(input())
	for n in range(N):
		H,W=map(int,sys.stdin.readline().strip().split())
		M=[map(int,sys.stdin.readline().strip().split()) for h in range(H)]
		M=solve(M)
		print "Case #{}: \n{}".format(n+1,
			"\n".join([" ".join(map(str,r)) for r in M]))

def C():
	def solve(S):
		P="welcome to code jam"
		M=[[0 for y in xrange(len(S))] for x in xrange(len(P))]
		for x in xrange(len(P)):
			for y in xrange(len(S)):
				if S[y]==P[x]:
					if x>0:
						M[x][y]=sum([M[x-1][t] for t in xrange(y)])%10000
					else:
						M[x][y]=1
		return sum(M[-1])%10000

	N=int(input())
	for n in range(N):
		S=sys.stdin.readline().strip()
		s=solve(S)
		print "Case #{}: {:0>4.0f}".format(n+1,s)

C()
