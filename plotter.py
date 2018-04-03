import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.interpolate import CubicSpline
from scipy.interpolate import UnivariateSpline
from scipy.optimize import curve_fit

def line(x,a,c):
    return x*b+c

rc('font',**{'family':'sans-serif','sans-serif':['Computer Modern Roman','Helvetica']})#makes the plots have pretty fonts
rc('text', usetex=True)

fluxes = np.loadtxt('fluxes.txt',skiprows=1)#load fluxes from file
print("fluxes={0}".format(fluxes))

spline = CubicSpline(np.log(fluxes[:,0]),np.log(fluxes[:,1]))
uspline = UnivariateSpline(np.log(fluxes[:,0]),np.log(fluxes[:,1]))
xspline = np.arange(np.amin(np.log(fluxes[:,0])), np.max(np.log(fluxes[:,0])),0.01)
line1 =  np.polyfit( np.log(fluxes[0:3,0]),np.log(fluxes[0:3,1]),1)
line2 =  np.polyfit(np.log(fluxes[2:6,0]),np.log(fluxes[2:6,1]),1)
x1 =  np.arange(np.amin(np.log(fluxes[0:3,0])), np.max(np.log(fluxes[0:3,0])),0.01)
x2 =  np.arange(np.amin(np.log(fluxes[2:6,0])), np.max(np.log(fluxes[2:6,0])),0.01)
p1 = np.poly1d(line1)
p2 = np.poly1d(line2)

fig1 = plt.figure()#plot fluxes
ax1 = fig1.add_subplot(111)
ax1.errorbar(np.log(fluxes[:,0]),np.log(fluxes[:,1]),yerr=np.multiply(np.divide(np.log(fluxes[:,1]),fluxes[:,1]),fluxes[:,2]),fmt='o')
#print(xspline)
#print(spline(xspline))
ax1.plot(xspline,spline(xspline))
#ax1.plot(xspline,uspline(xspline))
#ax1.plot(x1,p1(x1), x2, p2(x2))
ax1.set_title(r"Continuum Spectrum")
ax1.set_xlabel(r"$\ln(\nu$ [GHz])")
ax1.set_ylabel(r"$\ln$(Flux Density [$\mu$Jy])")
ax1.legend(["Cubic Spline","Measured Flux Density"], loc='best')
fig1.savefig('fluxVsFreq.png', bbox_inches='tight', dpi=300)
#plt.legend()
#plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(xspline,spline.derivative(1)(xspline))
#ax2.plot(xspline,uspline.derivative()(xspline))
ax2.set_title(r"Spectral index as a function of frequency")
ax2.set_xlabel(r"$\ln(\nu$ [GHz])")
ax2.set_ylabel(r"$\alpha$")
ax2.legend(["Derivative of Cubic Spline"], loc='best')
fig2.savefig('spectral index.png', bbox_inches='tight', dpi=300)
plt.show()
