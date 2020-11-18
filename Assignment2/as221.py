# import os
# import pandas as pd

# a = pd.read_csv('dataa.txt')
# a.values.tolist()
# print(a)
# # cd "Downloads\Z-FODS F320\Assignment"
# # print(a[0])

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
w=[]
for i in range (0,len(powers)):
    w.append(0)

alpha = 0.000001
thres = 10**-10
lambdaa=0.0001
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




def train_model(w):
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


iteration=0
curr=error1(w)
prev=0
while(iteration<300):
    valuesreturned=train_model(w)
    for j in range (0,len(w)):
        w[j]=w[j]-alpha*valuesreturned[j]
    prev=curr
    curr=error1(w)
    print(iteration,prev)
    iteration+=1
    
    # if(abs(prev-curr)<thres):
    #     break

print(w)


# rmse calculation
r=0
r1=0
for i in range (d,len(b)):
    k=0
    k1=0
    for j in range (0,len(powers)):
        k+=w[j]*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
        k1+=w[j]*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
    k-=b[i][3]
    k1-=b[i][3]
    k1=k1*(max1[3]-min1[3])+min1[3]
    k1=k1**2
    k=k**2
    r+=k
    r1+=k1
r/=(len(b)-d)
r1/=(len(b)-d)
r1=r1**0.5
r=r**0.5
print(r)
print(r1)


#calculation of r squared
sse=0
for i in range (d,len(b)):
    sse0=0
    for j in range (0,len(powers)):
        sse0+=w[j]*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
    sse0-=b[i][3]
    sse0=sse0**2
    sse+=sse0
ts=0
# calculating y bar
for i in range (d,len(b)):
    ts+=b[i][3]
ts=ts/(len(b)-d)
tss=0
for i in range (d,len(b)):
    tss+=((ts-b[i][3])**2)
r2=1-(sse/tss)
print(r2)



# Now calculating using diff formula
sse=0
for i in range (d,len(b)):
    sse0=0
    for j in range (0,len(powers)):
        sse0+=w[j]*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
    sse0-=b[i][3]
    sse0=sse0**2
    sse+=sse0

ts=0
for i in range (d,len(b)):
    ts0=0
    for j in range (0,len(powers)):
        ts0+=w[j]*pow(b[i][1],powers[j][1])*pow(b[i][2],powers[j][2])
    ts+=ts0

ts=ts/(len(b)-d)

tss=0
for i in range (d,len(b)):
    tss+=((ts-b[i][3])**2)
r2=1-(sse/tss)
print(r2)










