import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
from tabulate import tabulate
# For Graphical  Representation
x2= np.linspace(1,3,100)
r2= np.linspace(1,3,100)
ro = -x2**r2
simp=((r2)*((x2)**(r2-1)))*(np.exp(ro))
fig , a = plt.subplots(figsize=(10,5))
plt.grid()
a.plot(r2,simp)
plt.fill_between(r2,simp)
a.set_ylim(0)
a.set_title('Weibull Distribution',size='30')
a.set_ylabel('Probability',size='20')
plt.show()


def weibullDistribution(x,r):
    # we are using standard weibull distribution that's why a will be 1 and U will be 0 so the formula for for density function will be the one down below
    # r*x**(r-1)*np.exp(-(x**r))
    ro = -x**r
    return ((r)*((x)**(r-1)))*(np.exp(ro))
    

def Simpson38(a,b,h):
    xi = []
    yi = []
    r= np.linspace(h,b,n+1)
    
    for i in range(0,n+1):
        x = x0 +i*h
        
        xi.append(x)
        if (x >0):
            y = weibullDistribution(xi[i],r[i])
        else :
            print("The Value Of X must be greater then 0")
        yi.append(y)
    for i in range(len(yi)):
        table = [ ['R% d'%(i),'X% d'%(i),'Y% d'%(i)],[r[i],xi[i],yi[i]]]
        print("\n")
        print(tabulate(table))
        
    
    formula= weibullDistribution(a,r[0]) + weibullDistribution(b,r[n])
    for i in range(1, n):
        if (i % 3 == 0):
            formula = formula + 2 * yi[i]
        else:
            formula = formula + 3 * yi[i]
    result = ((3*h)/8)*formula
   
    print('The Value Of The Integral Is F(x)= %0.6f'%(result))
    


print("Enter The Value Of Lower Limit")
a = float(input())
print("Enter The Value Of Upper Limit")
b = float(input())
print("Enter The Value Of N")
n = int(input())
h = (b-a)/3n
x0 = a
simpsonshort=Simpson38(a,b,h)


# for plotting only
x= np.linspace(a,b,n+1)
r= np.linspace(a,b,n+1)

plt.axvspan(0,simpsonshort,color='green',alpha=0)
plt.plot(r,weibullDistribution(x,r),'green')
plt.grid()
plt.scatter(0,0)
plt.show()


