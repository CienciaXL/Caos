import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(10,8), facecolor='w', edgecolor='k')
xdata, ydata = [], []
ln, = plt.plot([], [], 'b.', markersize=8, alpha=1)
#ln, = plt.plot([], [], 'b.', markersize=8, alpha=0.1)
colors = ['b', 'r', 'g', 'm', 'c','orange']

fig.patch.set_facecolor((0,0,0))
ax.set_facecolor((0, 0, 0))
ax.spines['bottom'].set_color((1,1,1))
ax.spines['top'].set_color((1,1,1))
ax.spines['right'].set_color((1,1,1))
ax.spines['left'].set_color((1,1,1))
ax.yaxis.label.set_color((1,1,1))
ax.xaxis.label.set_color((1,1,1))
ax.tick_params(axis='x', colors=(1,1,1))
ax.tick_params(axis='y', colors=(1,1,1))

GetNext = lambda r,x : r*x*(1-x)

def GetAssymp(r, x0=0.5, N=200):
  x = x0
  for i in range(N): 
    x = GetNext(r,x)
  return x

import random
GetRandomX = lambda : random.uniform(0., 1)

### Convergencia
class RandomVar:
  def __init__(self,_x=0.5):
    self.x=_x
    if self.x == -1: self.SetRandom
  def SetRandom(self):
    self.x = random.uniform(0, 1.)
    
r = [0.4, 0.8, 1.5, 2.5, 3.3, 3.5, 3.8, 3.9]
N = 20
ymax = 1
rounds=5*len(r)
ntext = ax.text(float(N)/3, -0.1, 'x$_{%i+1}$ = kx$_{%i}$(1-x$_%i$) = %1.2f'%(0,0,0,0), fontsize=16, color='w')
xr = RandomVar()

###################################################################
### Parametros
xmin, xmax = [0,4]
ymin, ymax = [-0.1,1]
n = 800

def InitCurve():
  ax.set(xlabel='k', ylabel='x$_N$', title='')
  ax.set_xlim(xmin, xmax)
  ax.set_ylim(ymin, ymax)
  return ln,

def UpdateCurve(r):
  for i in range(10):
    xr.SetRandom()
    x0 = xr.x
    xdata.append(r)
    ydata.append(GetAssymp(r,x0))
  ln.set_data(xdata, ydata)
  ln.set_color('orange')
  return ln,

# Curva
ani = FuncAnimation(fig, UpdateCurve, frames=np.linspace(xmin, xmax, n),init_func=InitCurve, interval=10, blit=True)
#ani.save('xvsr_0to3.mp4', fps=30, dpi=300, savefig_kwargs={'facecolor':'black'})

plt.show()
