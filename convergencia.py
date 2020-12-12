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

class RandomVar:
  def __init__(self,_x=0.5):
    self.x=_x
    if self.x == -1: self.SetRandom
  def SetRandom(self):
    self.x = random.uniform(0, 1.)
    
### Parametros
r = [0.4, 0.8, 1.5, 2.5, 3.3, 3.5, 3.8, 3.9]
N = 20
ymax = 1
rounds=5*len(r)
ntext = ax.text(float(N)/3, -0.1, 'x$_{%i+1}$ = kx$_{%i}$(1-x$_%i$) = %1.2f'%(0,0,0,0), fontsize=16, color='w')
xr = RandomVar()

def InitConverg():
  ax.set_xlim(-0.5, N)
  ax.set_ylim(-0.2, ymax)
  ax.set(xlabel='N', ylabel='x$_N$', title='Convergencia')
  #ax.text(5, ymax*0.9, 'x$_{0}$ = %1.2f'%x, fontsize=20)
  return ln,

rtext = ax.text(1, -0.1, 'k = %1.2f'%r[0], fontsize=16, color='w')
def UpdateConverg(i):
  ir = int(i/(N*rounds/len(r)))
  i = i%N
  if i==0:
    xdata.clear()
    ydata.clear()
    xr.SetRandom()
    ln.set_color(colors[int(random.uniform(0, len(colors)))])
  xdata.append(i)
  xi = GetAssymp(r[ir],xr.x,i)
  ydata.append(xi)
  ntext.set_text('x$_{%i+1}$ = kx$_{%i}$(1-x$_{%i}$) = %1.2f'%(i, i, i ,xi))
  rtext.set_text('k = %1.2f'%r[ir])
  ln.set_data(xdata, ydata)
  return ln,ntext,rtext

###################################################################
ani = FuncAnimation(fig, UpdateConverg, frames=range(N*rounds),init_func=InitConverg, blit=False)
#ani.save('convergence.mp4', fps=5, dpi=300, savefig_kwargs={'facecolor':'black'})

plt.show()
