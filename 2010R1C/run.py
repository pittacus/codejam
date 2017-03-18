import sys

# Round 1C 2010
# https://code.google.com/codejam/contest/619102/dashboard#s=p0

def A():
	def solve(M):
		A=sorted(range(len(M)), key=lambda k: M[k][0])
		B=sorted(range(len(M)), key=lambda k: M[k][1])
		return sum([len(set(B[:B.index(A[x])]).intersection(set(A[x+1:])))
			for x in xrange(len(A))])

	T=int(input())
	for t in range(T):
		N=int(input())
		M=[map(int,sys.stdin.readline().strip().split()) for n in range(N)]
		s=solve(M)
		print "Case #{}: {}".format(t+1,s)

def B():
	def solve(L,P,C):
		import math
		s=-1
		while L<P:
			L*=C
			s+=1
		n=0
		while s:
			s/=2
			n+=1
		return n

	N=int(input())
	for n in range(N):
		L,P,C=map(int,sys.stdin.readline().strip().split())
		s=solve(L,P,C)
		print "Case #{}: {}".format(n+1,s)

def C():
	def solve(M):
		def bitmap(M,x,y):
			return ( M[x][y/4] & (1<<((3-y)%4)) )>0
		H=len(M)
		W=len(M[0])*4
		D={}
		Z=min(H,W)
		for z in xrange(1,Z+1):
			D[z]=set()
			for x in xrange(H):
				for y in xrange(W):
					if z==1:
						D[z].add((x,y))
					else:
						f= (x+z<=H and y+z<=W) and (x,y) in D[z-1] and (x+1,y) in D[z-1] and (x,y+1) in D[z-1] and (x+1,y+1) in D[z-1]
						f=f and (bitmap(M,x,y) == bitmap(M,x+1,y+1)) and (bitmap(M,x,y) != bitmap(M,x+1,y)) and (bitmap(M,x,y) != bitmap(M,x,y+1))
						if f: D[z].add((x,y))
			if len(D[z])==0:
				Z=z-1
				break

		S=[[0 for y in xrange(W)] for x in xrange(H)]
		C=[0 for x in xrange(Z+1)]
		for z in xrange(Z,0,-1):
			for x,y in sorted(D[z]):
				if S[x][y]==1 or S[x+z-1][y+z-1]==1 or S[x+z-1][y]==1 or S[x][y+z-1]==1: continue
				#print H,W,x,y,z,S[x][y],S[x+z-1][y+z-1]
				for px in xrange(x,x+z):
					for py in xrange(y,y+z):
						S[px][py]=1
				C[z]+=1
				#if z==6: print '\n'.join([''.join(['O' if S[x][y] else (' ' if bitmap(M,x,y) else '#') for y in xrange(W)]) for x in xrange(H)])
		#print C
		#print '\n'.join([''.join(['X' if bitmap(M,x,y) else ' ' for y in xrange(W)]) for x in xrange(H)])
		s=list(reversed(list(enumerate(C))[1:]))
		s=[t for t in s if t[1]]
		return s

	N=int(input())
	for n in range(N):
		H,W=map(int,sys.stdin.readline().strip().split())
		def hexmap(x):
			if '0'<=x<='9':
				return ord(x)-ord('0')
			else:
				return ord(x)-ord('A')+10
		M=[map(hexmap,list(sys.stdin.readline().strip())) for h in xrange(H)]
		s=solve(M)
		print "Case #{}: {}\n{}".format(n+1,len(s),"\n".join([" ".join(map(str,t)) for t in s]))

C()
