from mpmath import * 
import csv
import math
from math import pi, log, factorial
from decimal import Decimal, getcontext
import time
f1=time.perf_counter()



#
#From pg 116
#Scientific American 
#February 1988
#Ramanujan and Pi

mp.dps = 10000100
mp.pretty = True
s1 = nthroot(2,2)
s2 = fmul(4,s1)
Alpha0= fsub(6,s2)

Y0 = fsub(s1,1)

y1=power(Y0,4)
y2=fsub(1,y1)
y3=nthroot(y2,4)
y4=fadd(1,y3)
y5=fsub(1,y3)

YOne= fdiv(y5,y4)


print("Start Loop")

for x in range(1,12):
#7 iterations should give 15K digits
#16 iterations should give 2 billion digits
	N= (2*x+1)
	M=(2**N)

	AlphaT2=fmul(YOne, YOne)
	AlphaT3= fadd(AlphaT2, YOne)
	AlphaT4= fadd(AlphaT3,1)
	AlphaT5= fmul(AlphaT4,YOne)
	AlphaT6 = fmul(M, AlphaT5)


	AlphaT7= fadd(1, YOne)
	AlphaT8= power(AlphaT7,4)
	AlphaT9=fmul(AlphaT8,Alpha0)


	Alpha1= fsub(AlphaT9,AlphaT6)
	Alpha0 = Alpha1

	YS1= power(YOne,4)
	YS2= fsub(1,YS1)
	YT1= nthroot(YS2,4)


	YS3= fadd(1,YT1)
	YS4 = fsub(1,YT1)
	YOne = fdiv(YS4,YS3)


print("Loop Done")
MyPi=fdiv(1,Alpha1)

with open('D:\Python\Check\RawPi\MyPi.txt', 'w') as fp:
    writer = csv.writer(fp)
    fp.write(nstr(MyPi,n=1000001))

f2=time.perf_counter()
print("Execustion time:", f2-f1)