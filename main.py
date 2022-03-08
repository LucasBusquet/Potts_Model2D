
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import copy

##################################################################################################
nx = 100
ny = 100
Temp=1

n_levels=50

fig = plt.figure()
data = np.zeros((nx, ny))
data=[[random.randint(0,n_levels-1) for i in range(nx)] for i in range(ny)]
data=np.array(data)
im = plt.imshow(data)
def init():
    global data
    im.set_data(data)



def animate(i):
    global data
    #print(i)
    data=next_state(data)
    im.set_data(data)
    return im

def next_state(data):
    for i in range(10000):
        n=random.randint(0, nx-1)
        m=random.randint(0,ny-1)
        next=random.randint(0,n_levels-1);
        a=(data[m][(n-1+nx)%nx]==next)*2-1
        b=(data[m][(n+1)%nx]==next)*2-1
        c=(data[(m-1+ny)%ny][n]==next)*2-1
        d=(data[(m+1)%ny][n]==next)*2-1

        d1 = (data[(m + 1) % ny][(n + 1) % nx] == next) * 2 - 1
        d2 = (data[(m + 1) % ny][(n - 1 + nx) % nx] == next) * 2 - 1
        d3 = (data[(m - 1 + ny) % ny][(n + 1) % nx] == next) * 2 - 1
        d4 = (data[(m - 1 + ny) % ny][(n - 1 + nx) % nx] == next) * 2 - 1

        E=a+b+c+d+d1+d2+d3+d4

        if E > 0:
            data[m][n] = next;
        else:
            r=np.random.uniform();
            if E <= 0 and r < np.exp(E / Temp):
                rand = random.randint(0,3)
                if rand == 0:
                    data[m][n] = data[m][n-1]
                elif rand == 1:
                    if n+1 >= nx:
                        data[m][n] = data[m][0]
                    else:
                        data[m][n] = data[m][n+1]
                elif rand == 2:
                    if m+1 >= ny:
                        data[m][n] = data[0][n]
                    else:
                        data[m][n] = data[m+1][n]
                elif rand == 3:
                    data[m][n] = data[m-1][n]

    return data



anim = animation.FuncAnimation(fig, animate, init_func=init, frames=800,interval=10)

plt.show()
