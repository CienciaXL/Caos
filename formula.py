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

###################################################################
### Parametros
N = 50
r = 3.5 
x0 = 0.4
xmin, xmax = [0,4]
ymin, ymax = [-0.1,1]

ntext = ax.text(float(N)/3, -0.1, 'x$_{%i+1}$ = kx$_{%i}$(1-x$_%i$) = %1.2f'%(0,0,0,0), fontsize=16, color='w')
rtext = ax.text(10, 1.05, 'k = %1.2f'%r, fontsize=16, color='w')
xtext = ax.text(80, 1.05, 'x$_0$ = %1.1f'%x0, fontsize=16, color='w')
def InitConvergN():
  ax.set_xlim(-0.5, N)
  ax.set_ylim(-0.2, ymax)
  ax.set(xlabel='N', ylabel='x$_N$', title='')
  #ax.text(5, ymax*0.9, 'x$_{0}$ = %1.2f'%x, fontsize=20)
  return ln,

def UpdateConvergN(i):
  xdata.append(i)
  xi = GetAssymp(r,x0,i)
  ydata.append(xi)
  ntext.set_text('x$_{%i+1}$ = kx$_{%i}$(1-x$_{%i}$) = %1.2f'%(i, i, i ,xi))
  #rtext.set_text('r = %1.2f'%r)
  ln.set_data(xdata, ydata)
  ln.set_color('y')
  return ln,ntext,rtext


###################################################################
ani = FuncAnimation(fig, UpdateConvergN, frames=range(N),init_func=InitConvergN, blit=False)
#ani.save('x200forx04.mp4', fps=24, dpi=300, savefig_kwargs={'facecolor':'black'})

plt.show()
