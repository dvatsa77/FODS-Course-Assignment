# import os
# import pandas as pd

# a = pd.read_csv('dataa.txt')
# a.values.tolist()
# print(a)
# # cd "Downloads\Z-FODS F320\Assignment"
# # print(a[0])

import matplotlib.pyplot as plt
import matplotlib.ticker as mt
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

# defining lambda as t
t=0.0001



def error0(p,q,r,lambdaa):
    e0=0
    e1=0
    e2=0
    i=0
    while(i<d):
        e0 += (p + q*b[i][1] + r*b[i][2] - b[i][3])
        e1 += (p + q*b[i][1] + r*b[i][2] - b[i][3]) * b[i][1]
        e2 += (p + q*b[i][1] + r*b[i][2] - b[i][3]) * b[i][2]
        i=i+1
    return e0+2*lambdaa*p, e1+2*lambdaa*q, e2+2*lambdaa*r





prev=-10
def calculatingregulariztionforlambdaa(lambdaa):
    w0=0
    w1=0
    w2=0
    i=0
    while(i<100):
        a0=w0
        a1=w1
        a2=w2
        e0, e1, e2=error0(a0,a1,a2,lambdaa)
        w0 -= n * e0
        w1 -= n * e1
        w2 -= n * e2
        i += 1
    return w0,w1,w2



def rmsecalculation(w0,w1,w2):
    r1=0
    for i in range (d,len(b)):
        r1+=((b[i][3]-w0-w1*b[i][1]-w2*b[i][2])**2)
    r1=r1/(len(b)-d)
    r1=r1**(0.5)
    return r1

def regularizingDegree6():
    lambdaa=0.0001
    xaxiss=[]
    yaxiss=[]
    for i in range (0,11):
        w0,w1,w2=calculatingregulariztionforlambdaa(lambdaa)
        r=rmsecalculation(w0,w1,w2)
        xaxiss.append(lambdaa)
        yaxiss.append(r)
        lambdaa+=0.0001
    
    plt.plot(xaxiss,yaxiss)
    plt.ylim(0,1)
    plt.xlim(0,0.001)

    plt.show()







    






        


