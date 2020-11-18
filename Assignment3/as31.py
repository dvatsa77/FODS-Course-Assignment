import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt
import matplotlib.ticker as mt
import random
dataset =[]
for i in range (0,112):
    dataset.append(1)
for i in range (112,160):
    dataset.append(0)
dataset=np.asarray(dataset)
# print(len(dataset))
# print(np.sum(dataset))
random.shuffle(dataset)
def gamma1(a,b):
    gam=gamma(a+b)
    return gam

def gamma2(a):
    gam=gamma(a)
    return gam

a=[]
b=[]
ak=4
bk=6
a.append(ak)
b.append(bk)


for i in range (0,160):
    if(dataset[i]==1):
        ak+=1
    else:
        bk+=1
    if((i+1)%20==0):
        a.append(ak)
        b.append(bk)

print(5)

def gettingdistributionvalue(mean,a,b):
    # likelihood_prob=pow(mean,112)*pow(1-mean,48)
    priority_prob=(gamma(a+b)/(gamma(a)*gamma(b)))*pow(mean,a-1)*pow(1-mean,b-1)
    return priority_prob

def plot(a,b):
    meu=0
    xaxiss=[]
    yaxiss=[]
    for i in range (0,100):
        k=gettingdistributionvalue(meu,a,b)
        xaxiss.append(meu)
        yaxiss.append(k)
        meu+=0.01
    
    plt.plot(xaxiss,yaxiss)

    plt.show()




for i in range (0,len(a)):
    plot(a[i],b[i])



