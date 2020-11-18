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



# calculating powers matrix
powers=[]
pq=0
pqr=0
c=0
n=2
for pq in range (0,n+1):
    for pqr in range (0,n-pq+1):
        powers.append([pq,pqr,n-pq-pqr])
print(powers)
# exit(1)


alpha = 0.000001
thres = 10**-10
# y = w0 + w1*a[i][1]+w2*a[i][2]
d=int(len(a)*0.7)

# defining squared error function
def error1(w):
    e=0
    
    for i in range (0,d):
        k=-b[i][3]
        for j in range (0,len(powers)):
            k+=w[j]*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
        
        k=k**2
        e+=k
    e=e/2
    return e




def train_model(w,lambdaa):
    # e=error1(w)
    e0=[]
    for i in range (0,len(powers)):
        e0.append(0)
    
    for i in range (0,d):
        e=-b[i][3]
        for j in range (0,len(powers)):
            e+=w[j]*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
        
        for j in range (0,len(powers)):
            e0[j]+=e*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
    for j in range (0,len(powers)):
        e0[j]+=w[j]*lambdaa*2
    return e0




# prev=0
def traingourmodelfordifferentlambda(lambdaa):
    iteration=0
    w=[]
    for i in range (0,len(powers)):
        w.append(0)
    while(iteration<50):
        valuesreturned=train_model(w,lambdaa)
        for j in range (0,len(w)):
            w[j]=w[j]-alpha*valuesreturned[j]
        # prev=curr
        # curr=error1(w)
        # print(iteration,prev)
        iteration+=1
    return w




# rmse calculation
def rmsecalculation(w):
    r=0
    
    for i in range (d,len(b)):
        k=0
        for j in range (0,len(powers)):
            k+=w[j]*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
        k-=b[i][3]
        k=k**2
        r+=k
    r/=(len(b)-d)
    r=r**0.5
    return r
# print(r)
# print(r1)



# regularizing for different values of lambdaa
def regularizingDegree6():
    lambdaa=0.0001
    xaxiss=[]
    yaxiss=[]
    w=[]
    for i in range (0,11):
        w=traingourmodelfordifferentlambda(lambdaa)
        r=rmsecalculation(w)
        xaxiss.append(lambdaa)
        yaxiss.append(r)
        lambdaa+=0.0001
    
    plt.plot(xaxiss,yaxiss)
    plt.ylim(0,1)
    plt.xlim(0,0.001)

    plt.show()

regularizingDegree6()






















































