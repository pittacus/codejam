import sys

# Round 1A 2010
# https://code.google.com/codejam/contest/544101/dashboard#s=p2&a=1

def A():
	def rotate(M):
		for m in M: m.sort(lambda x,y: -1 if x=='.' else 0 if y=='.' else 1)
		return M

	def check(M,K):
		N=len(M)
		R=range(N)
		s=[]
		s+=["".join(M[x]) for x in R]
		s+=["".join([M[x][y] for x in R]) for y in R]
		s+=["".join([M[x+t][t] for t in range(N-x)]) for x in R]
		s+=["".join([M[x][x+t] for x in range(N-t)]) for t in R]
		s+=["".join([M[y+t][y] for y in range(N-t)]) for t in R]
		s+=["".join([M[x][t-x] for x in range(t+1)]) for t in R]
		s+=["".join([M[x][N+t-x-1] for x in range(t,N)]) for t in R]
		R=[x for x in set(s) if x.find("R"*K)>=0]
		B=[x for x in set(s) if x.find("B"*K)>=0]
		if B and R:
			return 'Both'
		elif B:
			return 'Blue'
		elif R:
			return 'Red'
		else:
			return 'Neither'

	T=int(input())
	for t in range(T):
		N,K=map(int,sys.stdin.readline().strip().split())
		M=[list(sys.stdin.readline().strip()) for n in range(N)]
		M=rotate(M)
		s=check(M,K)
		print "Case #{}: {}".format(t+1,s)

def B():
	def solve(A,D,I,M):
		def interp(p,t,M,I):
			import math
			s=(abs(p-t)-1)//M*I
			#print p,t,M,I,s
			return s if s>0 else 0

		C=[[0 for x in range(256)] for y in range(256)]
		for k in range(1,len(A)+1):
			for p in range(256):
				if M==0:
					C[k][p]=min(C[k-2][p]+D,C[k-1][p])+abs(A[k-1]-p)
				else:
					C[k][p]=min([ C[k-2][p]+D ]
					+[C[k-1][t]+interp(p,t,M,I) for t in range(256)]
					)+abs(A[k-1]-p)
		return min(min(C[len(A)]), min(C[len(A)-1])+D)
	def solve2(A,D,I,M):
		#print A,D,I,M
		C=[0]*256
		for a in A:
			if M==0:
				C=[min(C[i]+D,C[i]+abs(a-i)) for i in range(256)]
			else:
				C=[min(C[i]+D, min([C[j]+abs(a-i)+max(abs(j-i)-1,0) // M * I for j in range(256)])) for i in range(256)]
		#print D,I,M,a,C[:10]
		return min(C)
	T=input()
	for t in range(T):
		D,I,M,N=map(int,raw_input().split())
		A=map(int,raw_input().split())
		#if t+1!=1: continue
		#print D,I,M,A
		s=solve2(A,D,I,M)
		print "Case #{}: {}".format(t+1,s)

def C():
	def win(A,B):
		if A<B: A,B=B,A
		if A>=2*B: return True
		if A==B: return False
		return not win(B,A-B)

	# for x in range(30):
	# 	print x,"**",
	# 	for y in range(30):
	# 		print y%10 if win(x,y) else 'X',
	# 	print
	def findL(A):
		L,U=A//2,A
		while L+1<U:
			M=max((L+U)//2,L+1)
			#print A,L,M,U
			if win(A,M):
				L=M
			else:
				U=M
		return L
	def findU(A):
		L,U=A,2*A
		while L+1<U:
			M=min((L+U)//2,U-1)
			if win(A,M):
				U=M
			else:
				L=M
		return U
	#for A in range(30): print A,findL(A),findU(A)
	#return
	M={}
	def solve(A1,A2,B1,B2):
		s=0
		for A in range(A1,A2+1):
			if A in M:
				L,U=M[A]
			else:
				L,U=findL(A),findU(A)
				M[A]=(L,U)
			s+=max(min(B2,L)-B1+1,0)
			s+=max(B2-max(B1,U)+1,0)
			#print A,L,U,B1,B2,s
		return s
	for t in range(input()):
		A1,A2,B1,B2=map(int,raw_input().split())
		s=solve(A1,A2,B1,B2)
		print "Case #{}: {}".format(t+1,s)

C()
