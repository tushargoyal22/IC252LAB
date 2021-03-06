
import numpy as np
import matplotlib.pyplot as plt

f = plt.figure(figsize=(18, 10))
 
def plotHist(nr, N, n_, mean, var0, x0):
    ''' plots the RVs'''
    x = np.zeros((N))#array of zeroes
    sp = f.add_subplot(3, 2, n_ )#to make number of plots in a single plot
    #N is the number of samples,#nr is size of sample
    for i in range(N):    
        for j in range(nr):
            x[i] += np.random.uniform(0,1) 
        x[i] *= 1/nr
        
    plt.hist(x,100, normed=True, color='b', label=" %d RVs"%(nr));
#    plt.setp(sp.get_yticklabels(), visible=False)
    
    variance = var0/nr                     
    fac = 1/np.sqrt(2*np.pi*variance)
    dist = fac*np.exp(-(x0-mean)**2/(2*variance))
    plt.plot(x0,dist,color='r',linewidth=2,label='CLT',alpha=0.6)
    plt.xlabel('r')
    plt.xlim([0, 1])
    leg = plt.legend(loc="upper left")
#    leg.get_frame().set_alpha(0.1)

    
N = 1000000   # number of samples taken
nr = ([1, 2, 4, 8, 16, 32])#Size of Samples

mean, var0 = 0.5, 1.0/12  # mean and variance of uniform distribution in range 0, 1
x0 = np.linspace(0, 1, 200)

for i in range(np.size(nr)):
    plotHist(nr[i], N, i+1, mean, var0, x0)

plt.suptitle("Addition of uniform random variables (RVs) converge to a Gaussian distribution (CLT)",fontsize=20)
plt.savefig('rvs_clt.png')