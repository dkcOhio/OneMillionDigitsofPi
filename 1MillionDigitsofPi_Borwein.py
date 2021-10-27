from mpmath import * 
import csv
import math
from math import pi, log, factorial
from decimal import Decimal, getcontext
import time
f1=time.perf_counter()

#https://en.wikipedia.org/wiki/Borwein%27s_algorithm
#Nonic convergence
#http://www.hvks.com/Numerical/Downloads/HVE%20Practical%20implementation%20of%20PI%20Algorithms.pdf
#PG 29
#Use Capital variables for final calc
#Use lower case variblbes for intermediate calcs
#7 iterations give 1M in 11 seconds
mp.dps = 1000100
mp.pretty = True

A0 =fdiv(1,3)

r1 = nthroot(3,2)
r2=fsub(r1,1)
R0 = fdiv(r2,2)

s0 = power(R0,3)
s1 = fsub(1,s0)
S0 = nthroot(s1,3)

print("Start Loop")
for k in range(0,7):
	t1 = fmul(R0,2)
	T1 = fadd(1,t1)


	u1 = power(R0,2)
	u2 = fadd(u1,R0)
	u3 = fadd(u2,1)
	u4 = fmul(9,R0)
	u5 = fmul(u4,u3)
	U1 = nthroot(u5,3)
	

	v1= power(U1,2)
	v2 = fmul(T1,U1)
	v3= power(T1,2)
	v4 = fadd(v1,v2)
	V1= fadd(v4,v3)

	w1 = power(S0,2)
	w2 = fadd(w1,S0)
	w3 = fadd(1,w2)
	w4= fmul(27, w3)
	W1 = fdiv(w4,V1)

	a1 = fsub(1,W1)
	a2 =  fmul(2,k)
	a3 = fsub(a2,1)
	a4 = power(3,a3)
	a5= fmul(a4,a1)
	a6= fmul(W1,A0)
	A1 = fadd(a6,a5)

	s1 = fsub(1,R0)
	s2 = power(s1,3) 
	s3 = fmul(2,U1)
	s4 = fadd(T1,s3)
	s5 = fmul(s4,V1)
	S1 = fdiv(s2,s5)

	r1 = power(S1,3)
	r2 = fsub(1,r1)
	R1 = nthroot(r2,3)

	R0=R1
	S0=S1
	A0=A1

print("Loop Done")
MyPi = fdiv(1,A1)
#print(MyPi)

with open('D:\Python\Borwein\Check\RawPi\MyPi1027.txt', 'w') as fp:
    writer = csv.writer(fp)
    fp.write(nstr(MyPi,n=1000001))

f2=time.perf_counter()
print("Execution time:", f2-f1)