import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.interpolate import CubicSpline

rc('font',**{'family':'sans-serif','sans-serif':['Computer Modern Roman','Helvetica']})#makes the plots have pretty fonts
rc('text', usetex=True)

fluxes = np.loadtxt('fluxes.txt',skiprows=1)#load fluxes from file
print("fluxes={0}".format(fluxes))

spline = CubicSpline(np.log10(fluxes[:,0]),np.log10(fluxes[:,1]))
xspline = np.arange(np.amin(np.log10(fluxes[:,0])), np.max(np.log10(fluxes[:,0])),0.01)
fig1 = plt.figure()#plot fluxes
ax1 = fig1.add_subplot(111)
ax1.errorbar(np.log10(fluxes[:,0]),np.log10(fluxes[:,1]),yerr=np.log10(fluxes[:,2]),fmt='o')
#print(xspline)
#print(spline(xspline))
ax1.plot(xspline,spline(xspline))
ax1.set_title(r"Flux density as a function of frequency")
ax1.set_xlabel(r"$\log_{10}(\nu$ [GHz])")
ax1.set_ylabel(r"$\log_{10}$(Flux Density [uJy])")
ax1.legend(["Cubic Spline","Measured Flux Density"], loc='best')
fig1.savefig('fluxVsFreq.png')#, bbox_inches='tight')
#plt.legend()
plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(xspline,spline(xspline,1))
ax2.set_title(r"Spectral index as a function of frequency")
ax2.set_xlabel(r"$\log_{10}(\nu$ [GHz])")
ax2.set_ylabel(r"$\alpha$")
ax2.legend(["Derivative of Cubic Spline"], loc='best')
fig2.savefig('spectral index.png')#, bbox_inches='tight')
plt.show()
