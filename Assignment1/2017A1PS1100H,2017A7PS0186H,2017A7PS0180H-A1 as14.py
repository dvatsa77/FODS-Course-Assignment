# import os
# import pandas as pd

# a = pd.read_csv('dataa.txt')
# a.values.tolist()
# print(a)
# # cd "Downloads\Z-FODS F320\Assignment"
# # print(a[0])

import numpy as np

import scipy
from sklearn.metrics import r2_score
file=open('dataa.txt','r')
a=[[1,2,3,4]]
a.pop()
for each in file:
    each=each.split(',')
    a.append(each)

i=0
c=0
while(i<len(a)):
    a[i][0]=int(a[i][0],10)
    a[i][1]=float(a[i][1])
    a[i][2]=float(a[i][2])
    a[i][3]=float(a[i][3])
    i=i+1
# step size n = 0.005
# threshold thres = 10**-10

b=[]
b=a
min1 = [0, 0, 0, 0]
max1 = [0, 0, 0, 0]
min1[3]=a[0][3]
max1[3]=a[0][3]
min1[2]=a[0][2]
max1[2]=a[0][2]
min1[1]=a[0][1]
max1[1]=a[0][1]
for i in range (0,len(a)):
    if(a[i][3]>max1[3]):
        max1[3]=a[i][3]
    if(a[i][3]<min1[3]):
        min1[3]=a[i][3]
    if(a[i][2]>max1[2]):
        max1[2]=a[i][2]
    if(a[i][2]<min1[2]):
        min1[2]=a[i][2]
    if(a[i][1]>max1[1]):
        max1[1]=a[i][1]
    if(a[i][1]<min1[1]):
        min1[1]=a[i][1]






#normalizing the data
for i in range (0,len(a)):
    b[i][1]=(b[i][1]-min1[1])/(max1[1]-min1[1])
    b[i][2]=(b[i][2]-min1[2])/(max1[2]-min1[2])
    b[i][3]=(b[i][3]-min1[3])/(max1[3]-min1[3])


n = 0.000004
thres = 10**-10
# y = w0 + w1*a[i][1]+w2*a[i][2]
d=int(len(a)*0.7)


c=[]
for i in range(0, d):
    c.append([1,b[i][1],b[i][2]])


f=[]
j=0
for i in range (0,d):
    f.append(b[i][3])
    

c=np.asarray(c)
f=np.asarray(f)
e=np.array([])

e=(c.transpose())
e=np.matmul(e,c)
e=np.linalg.inv(e)
e=np.matmul(e,c.transpose())
e=np.matmul(e,f)
e=e.transpose()

print(e)
w0=e[0]
w1=e[1]
w2=e[2]


r=0
r1=0
for i in range (d,len(b)):
    r1+=((b[i][3]-w0-w1*b[i][1]-w2*b[i][2])**2)
r1=r1/(len(b)-d)
r1=r1**(0.5)
print(r1)


for i in range (d,len(b)):
    r+=(((b[i][3]-w0-w1*b[i][1]-w2*b[i][2])*(max1[3]-min1[3])+min1[3])**2)
r=r/(len(b)-d)
r=r**(0.5)
print(r)


print("R squared of test data is:-")

# R^2 = 1-(SSE/TSS)

sse=0
for i in range (d,len(b)):
    sse+=((b[i][3]-w0-w1*b[i][1]-w2*b[i][2])**2)
ts=0
for i in range (d,len(b)):
    ts+=w1*b[i][1]+w2*b[i][2]+w0
ts=ts/(len(b)-d)
tss=0
for i in range (d,len(b)):
    tss+=((ts-b[i][3])**2)
r2=1-(sse/tss)
print(r2)
# 678,4,-12
Y_pred=[]
Y_test=[]
for i in range (d,len(b)):
    Y_pred.append(b[i][3])
for i in range (d,len(b)):
    Y_test.append(w1*b[i][1]+w2*b[i][2]+w0)
print(r2_score(Y_test,Y_pred))
