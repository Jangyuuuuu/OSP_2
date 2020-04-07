#!/usr/bin/python

N=int(input("fibonacci number? "))

def fibo(n):
	b=True
	f1=1
	f2=1

	while n>2:
		if b:
			f1=f1+2
		else:
			f2=f1+f2
		b=not b
		n-=1
	if b:
		return f2
	else:
		return f1

for i in range(1,N):
	print(fibo(i),end=',')
print(fibo(N))

print("F%d = %d" % (N,fibo(N)))
